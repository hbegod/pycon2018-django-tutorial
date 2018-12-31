# TODO Тут наполнять урлами.
from django.urls import path, register_converter

from . import views, converters

register_converter(converters.emailConverter, 'email')

urlpatterns = [
    path('cart/', views.cart),
    path('shipping_form/', views.shipping_form),
    path('payment_form/', views.payment_form),
    path('success/', views.success),
    path('failure/', views.failure)

]