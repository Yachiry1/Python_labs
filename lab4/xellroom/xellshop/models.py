# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import timezone

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


class Address(models.Model):
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100)  # EmailField замість CharField
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # дата створення
    updated_at = models.DateTimeField(auto_now=True)      # дата оновлення
    slug = models.SlugField(unique=True, blank=True)      # можна використовувати для URL

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.first_name}-{self.last_name}")
            slug = base_slug
            counter = 1
            while Customer.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(
        'Orders',
        on_delete=models.CASCADE,  # якщо замовлення видалено, видаляємо позицію
        blank=True,
        null=True
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,  # якщо продукт видалено, залишаємо null
        blank=True,
        null=True
    )
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f"{self.product} x {self.quantity}"

class Orders(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,  # залишаємо замовлення, якщо клієнт видалений
        blank=True,
        null=True
    )
    order_date = models.DateTimeField(auto_now_add=True)  # дата створення замовлення
    status = models.ForeignKey(
        'Status',
        on_delete=models.SET_NULL,  # якщо статус видалено, залишаємо null
        blank=True,
        null=True,
        default=1
    )
    products = models.ManyToManyField(
        'Product',
        through='OrderItem',
        related_name='orders'
    )

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order #{self.status} - {self.customer}"

class Payment(models.Model):
    order = models.ForeignKey(
        Orders,
        on_delete=models.CASCADE,  # видаляємо платіж при видаленні замовлення
        blank=True,
        null=True
    )
    payment_date = models.DateTimeField(auto_now_add=True)  # дата створення платежу
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    status = models.ForeignKey(
        'Status',
        on_delete=models.SET_NULL,  # залишаємо null, якщо статус видалено
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'payment'
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return f"{self.method} - {self.amount}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(  auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'product'

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'review'
        unique_together = ('product', 'customer')
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"Review {self.rating} by {self.customer} for {self.product}"

class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'status'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name
