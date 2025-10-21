from xellshop.models import Orders
from .base_repository import BaseRepository

class OrdersRepository(BaseRepository):
    model = Orders