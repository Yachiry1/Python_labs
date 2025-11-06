from xellshop.models import OrderItem
from .base_repository import BaseRepository

class OrderItemRepository(BaseRepository):
    model = OrderItem