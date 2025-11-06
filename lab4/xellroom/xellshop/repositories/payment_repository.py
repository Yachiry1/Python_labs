from xellshop.models import Payment
from .base_repository import BaseRepository

class PaymentRepository(BaseRepository):
    model = Payment