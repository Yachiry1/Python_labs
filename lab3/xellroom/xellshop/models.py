# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import timezone

from django.db import models


class Address(models.Model):
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Customer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class OrderItem(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'order_item'


class Orders(models.Model):
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    status = models.ForeignKey('Status', models.DO_NOTHING, blank=True, null=True, default=1)

    class Meta:
        managed = False
        db_table = 'orders'


class Payment(models.Model):
    order = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    status_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True, default=1)

    class Meta:
        managed = False
        db_table = 'product'


class Review(models.Model):
    pk = models.CompositePrimaryKey('product_id', 'customer_id')
    product = models.ForeignKey(Product, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'
