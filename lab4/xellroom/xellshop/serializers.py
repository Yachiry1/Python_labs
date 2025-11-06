from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Product name must be at least 2 characters long")
        return value

    def validate(self, attrs):
        if attrs.get('price', 0) < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return attrs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'slug')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    # show nested product info if needed (optional)
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'product_id', 'quantity', 'unit_price')
        read_only_fields = ('id',)


class OrdersSerializer(serializers.ModelSerializer):
    # Read: include order items nested (read-only)
    order_items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source='customer', write_only=True, required=False, allow_null=True
    )
    status = StatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(), source='status', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Orders
        fields = (
            'id',
            'customer', 'customer_id',
            'order_date',
            'status', 'status_id',
            'order_items',
        )
        read_only_fields = ('id', 'order_date',)


class PaymentSerializer(serializers.ModelSerializer):
    order = OrdersSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Orders.objects.all(), source='order', write_only=True, required=False, allow_null=True
    )
    status = StatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(), source='status', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Payment
        fields = ('id', 'order', 'order_id', 'payment_date', 'amount', 'method', 'status', 'status_id')
        read_only_fields = ('id', 'payment_date')


class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source='customer', write_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'product', 'product_id', 'customer', 'customer_id', 'rating', 'comment', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

