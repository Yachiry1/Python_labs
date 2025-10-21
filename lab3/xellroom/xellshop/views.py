from django.http import HttpResponse
from django.shortcuts import render

from xellshop.models import Product
from xellshop.repositories.product_repository import ProductRepository


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def product(request):
    repo = ProductRepository()
    products = repo.get_all()
    return render(request, "product.html", {"product": products})

def product_by_id(request, product_id):
    repo = ProductRepository()
    products = repo.get_by_id(product_id)
    return render(request, "product_by_id.html", {"product": products})