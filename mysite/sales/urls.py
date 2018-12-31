# TODO Тут наполнять урлами.
from django.urls import path, register_converter

from . import views, converters

register_converter(converters.emailConverter, 'email')


urlpatterns = [
    path('sales/', views.sales),
    path('favorite/', views.favorite),
    path('category_analytic/<slug:category>/<email:user_email>', views.category_analytic)
]
