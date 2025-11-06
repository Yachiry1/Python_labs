from django.urls import path
from .views import (
    ProductApiView, CategoryApiView, CustomerApiView,
    AddressApiView, OrdersApiView, OrderItemApiView,
    PaymentApiView, ReviewApiView, StatusApiView, index, ReportView
)

urlpatterns = [
    path('', index),

    # products
    path('api/products/', ProductApiView.as_view()),
    path('api/products/<int:pk>/', ProductApiView.as_view()),

    # categories
    path('api/categories/', CategoryApiView.as_view()),
    path('api/categories/<int:pk>/', CategoryApiView.as_view()),

    # customers
    path('api/customers/', CustomerApiView.as_view()),
    path('api/customers/<int:pk>/', CustomerApiView.as_view()),

    # address
    path('api/addresses/', AddressApiView.as_view()),
    path('api/addresses/<int:pk>/', AddressApiView.as_view()),

    # orders
    path('api/orders/', OrdersApiView.as_view()),
    path('api/orders/<int:pk>/', OrdersApiView.as_view()),

    # order items
    path('api/order-items/', OrderItemApiView.as_view()),
    path('api/order-items/<int:pk>/', OrderItemApiView.as_view()),

    # payments
    path('api/payments/', PaymentApiView.as_view()),
    path('api/payments/<int:pk>/', PaymentApiView.as_view()),

    # reviews
    path('api/reviews/', ReviewApiView.as_view()),
    path('api/reviews/<int:pk>/', ReviewApiView.as_view()),

    # status
    path('api/statuses/', StatusApiView.as_view()),
    path('api/statuses/<int:pk>/', StatusApiView.as_view()),

    # report
    path('api/report/<int:pk>/', ReportView.as_view()),
    path('api/report/', ReportView.as_view()),
]