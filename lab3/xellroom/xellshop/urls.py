from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #http://127.0.0.1:8000/xellshop/
    path('product/', views.product), #http://127.0.0.1:8000/product/
    path('product/<int:product_id>/', views.product_by_id), #http://127.0.0.1:8000/product/id/
]