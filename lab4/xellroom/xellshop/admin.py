from django.contrib import admin
from rest_framework.views import APIView

from xellshop.models import Customer, Product


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "created_at",)
  prepopulated_fields = {"slug": ("first_name", "last_name")}

admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
  list_display = ("name", "price", "stock_quantity",)

admin.site.register(Product, ProductAdmin)