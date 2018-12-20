from django.db import models


class DirectorySuppliers(models.Model):
    name = models.CharField(max_length=30)


class DirectoryManufacturers(models.Model):
    name = models.CharField(max_length=30)


class DirectoryNomenclature(models.Model):
    nomenclature_name = models.CharField(max_length=30)
    manufacturers_name = models.OneToOneField(DirectoryManufacturers.name, on_delete=models.CASCADE)
    suppliers_name = models.OneToOneField(DirectorySuppliers.name.name, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30)


class DirectoryChecks(models.Model):
    Byers_name = models.CharField(max_length=30)

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

