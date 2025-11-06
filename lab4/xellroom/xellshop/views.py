from django.db.models import Count, Sum, Value, F, ExpressionWrapper
from django.db.models.functions import Coalesce
from django.forms import DecimalField
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from xellshop.repositories.product_repository import ProductRepository
from xellshop.repositories.customer_repository import CustomerRepository
from xellshop.repositories.category_repository import CategoryRepository
from xellshop.repositories.address_repository import AddressRepository
from xellshop.repositories.orders_repository import OrdersRepository
from xellshop.repositories.order_item_repository import OrderItemRepository
from xellshop.repositories.payment_repository import PaymentRepository
from xellshop.repositories.review_repository import ReviewRepository
from xellshop.repositories.status_repository import StatusRepository
from xellshop.serializers import *
from rest_framework import status

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#Base
class BaseApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    repo = None
    serializer_class = None

    def get(self, request, pk=None):
        if not self.repo or not self.serializer_class:
            return Response({'error': 'Repo or serializer not set'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if pk:
            obj = self.repo.get_by_id(pk)
            if not obj:
                return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
        else:
            objs = self.repo.get_all()
            serializer = self.serializer_class(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        obj = self.repo.create(request.data)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        if not self.repo.get_by_id(pk):
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        updated = self.repo.update_by_id(pk, request.data)
        serializer = self.serializer_class(updated)
        return Response(serializer.data)

    def delete(self, request, pk):
        success = self.repo.delete_by_id(pk)
        if not success:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

#Product
class ProductApiView(BaseApiView):
    repo = ProductRepository()
    serializer_class = ProductSerializer

#Customer
class CustomerApiView(BaseApiView):
    repo = CustomerRepository()
    serializer_class = CustomerSerializer

#Category
class CategoryApiView(BaseApiView):
    repo = CategoryRepository()
    serializer_class = CategorySerializer

#Address
class AddressApiView(BaseApiView):
    repo = AddressRepository()
    serializer_class = AddressSerializer

#Orders
class OrdersApiView(BaseApiView):
    repo = OrdersRepository()
    serializer_class = OrdersSerializer

#OrderItem
class OrderItemApiView(BaseApiView):
    repo = OrderItemRepository()
    serializer_class = OrderItemSerializer

#Payment
class PaymentApiView(BaseApiView):
    repo = PaymentRepository()
    serializer_class = PaymentSerializer

#Review
class ReviewApiView(BaseApiView):
    repo = ReviewRepository()
    serializer_class = ReviewSerializer

#Status
class StatusApiView(BaseApiView):
    repo = StatusRepository()
    serializer_class = StatusSerializer

#Report
class ReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Загальні лічильники
        total_customers = Customer.objects.count()
        total_orders = Orders.objects.count()
        total_products = Product.objects.count()
        total_payments = Payment.objects.count()
        total_reviews = Review.objects.count()
        total_categories = Category.objects.count()

        # Суми
        total_orders_value = OrderItem.objects.aggregate(
            total=Sum('unit_price')
        )['total'] or 0

        total_payments_value = Payment.objects.aggregate(
            total=Sum('amount')
        )['total'] or 0

        # Продукти за категоріями
        category_stats = Category.objects.annotate(
            total_products=Count('product'),
            total_value=Sum('product__price')
        ).values('name', 'total_products', 'total_value')

        report = {
            'general': {
                'total_customers': total_customers,
                'total_orders': total_orders,
                'total_products': total_products,
                'total_payments': total_payments,
                'total_reviews': total_reviews,
                'total_categories': total_categories
            },
            'sums': {
                'total_orders_value': total_orders_value,
                'total_payments_value': total_payments_value
            },
            'category_stats': list(category_stats)
        }

        return Response(report)