# xellshop/repositories/product_repository.py

from xellshop.models import Product
from .base_repository import BaseRepository

class ProductRepository(BaseRepository):
    def get_all(self):
        return Product.objects.all()

    def get_by_id(self, pk):
        return Product.objects.filter(id=pk).first()

    def create(self, data):
        return Product.objects.create(**data)

    def update_by_id(self, pk, data):
        Product.objects.filter(id=pk).update(**data)
        return Product.objects.filter(id=pk).first()

    def delete_by_id(self, pk):
        obj = Product.objects.filter(pk=pk)
        if not obj.exists():
            return None
        obj.delete()
        return True