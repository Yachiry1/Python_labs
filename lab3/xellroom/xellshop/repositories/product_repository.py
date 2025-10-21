# xellshop/repositories/product_repository.py

from xellshop.models import Product
from .base_repository import BaseRepository

class ProductRepository(BaseRepository):
    model = Product

    def get_expensive_products(self, min_price):
        return self.model.objects.filter(price__gte=min_price)
