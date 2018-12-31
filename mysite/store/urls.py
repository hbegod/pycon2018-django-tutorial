# TODO Тут наполнять урлами.
from django.urls import path, register_converter

from . import views, converters

register_converter(converters.dateConverter, 'date')

urlpatterns = [
    path('category/<int:name_or_id>', views.category),
    path('category/<slug:name_or_id>', views.category),
    path('product/<int:product_id>', views.product),
    path('incomes_list/', views.incomes_list),
    path('incomes_list/<int:income_type>', views.incomes_list),
    path('incomes_for_date/<date:admission_date>/', views.incomes_for_date),
    path('incomes_for_date/<date:admission_date>/<int:income_type>', views.incomes_for_date),
    path('income_page/<int:income_id>', views.income_page)
]