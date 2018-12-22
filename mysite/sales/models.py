from django.db import models


class DirectorySuppliers(models.Model):
    """
    Table with Suppliers
    """
    name = models.CharField(max_length=30)


class DirectoryManufacturers(models.Model):
    """
    Table with Manufacturers
    """
    name = models.CharField(max_length=30)


class DirectoryNomenclature(models.Model):
    """
    Nomenclature table
    Has one to one links to Suppliers and Manufacturers
    """
    nomenclature_name = models.CharField(max_length=30)
    manufacturers_name = models.OneToOneField(DirectoryManufacturers, on_delete=models.CASCADE)
    suppliers_name = models.OneToOneField(DirectorySuppliers, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30)


class DirectoryChecks(models.Model):
    """
    Table for Checks
    Has one to one link to Nomenclature
    Has price field
    Has sale_time and buyers_name field for sale control
    """
    buyers_name = models.CharField(max_length=30)
    sale_time = models.DateTimeField(auto_now_add=True)
    nomenclature_name = models.OneToOneField(DirectoryNomenclature, on_delete=models.CASCADE)
    prod_price = models.DecimalField(max_digits=8, decimal_places=2)

# TODO Модели добалять сюда.
# TODO  Необходимо сделать Django модели, которую будут покрывать логику.
# TODO
# TODO  Продавцы производят продажи.
# TODO  Продажи формируются на основе справочника номенклатуры.
# TODO  Для продаж необходим отслеживать, кем она изменена и когда.
# TODO  Для продаж формируеются чеки.
# TODO  Справочники номенлатуры формируется на основе
# TODO      справочника производителей.
# TODO      справочника справочника поставщиков.
# TODO
# TODO
# TODO  В докстрингах указать какая предпологается логика, работы с моделями.
# TODO
# TODO  Необходимо сформировать миграцию.

