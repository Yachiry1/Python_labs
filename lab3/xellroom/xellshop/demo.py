import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xellroom.settings")
django.setup()

from xellshop.repositories.customer_repository import CustomerRepository
from xellshop.repositories.product_repository import ProductRepository
from xellshop.repositories.orders_repository import OrdersRepository
from xellshop.repositories.category_repository import CategoryRepository

rc = CustomerRepository()
rp = ProductRepository()
ro = OrdersRepository()
rcat = CategoryRepository()

cat = rcat.get_by_id(1)

customer = rc.create(first_name="Mark", last_name="Trol", email="trol@example.com", phone="122056093")
product = rp.create(name="PowerBank", description="10000Mah", price=990, stock_quantity=9, category=cat)
order = ro.create(customer=customer)

print("Нова сутність Customer:", customer)
print("Нова сутність Product:", product)
print("Нова сутність Order:", order)

print("\nВсі користувачі:")
for c in rc.get_all():
    print(c.id, c.first_name, c.email)

print("\nВсі продукти:")
for p in rp.get_all():
    print(p.id, p.name, p.price)

print("\nВсі замовлення:")
for o in ro.get_all():
    print(o.id, o.customer, o.order_date, o.status)

print("\nВидаляємо створені записи...")

ro.delete(order)
rp.delete(product)
rc.delete(customer)

print("Видалення завершено.")

print("\nВсі користувачі після видалення:", rc.get_all())
print("Всі продукти після видалення:", rp.get_all())
print("Всі замовлення після видалення:", ro.get_all())