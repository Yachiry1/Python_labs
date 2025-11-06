from xellshop.models import Customer
from .base_repository import BaseRepository

class CustomerRepository(BaseRepository):
    def get_all(self):
        return Customer.objects.all()

    def get_by_id(self, pk):
        return Customer.objects.filter(id=pk).first()

    def create(self, data):
        return Customer.objects.create(**data)

    def update_by_id(self, pk, data):
        Customer.objects.filter(id=pk).update(**data)
        return Customer.objects.filter(id=pk).first()

    def delete_by_id(self, pk):
        obj = Customer.objects.filter(pk=pk)
        if not obj.exists():
            return None
        obj.delete()
        return True
