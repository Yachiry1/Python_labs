from xellshop.models import Customer
from .base_repository import BaseRepository

class CustomerRepository(BaseRepository):
    model = Customer