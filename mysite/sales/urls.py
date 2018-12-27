# TODO Тут наполнять урлами.
from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path('sales/', views.sales),
    path('favorite/', views.favorite),
    path('', views.category_analytic())
]
