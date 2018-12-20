from django.db import models


class DirectorySuppliers(models.Model):
    suppliers_name = models.CharField(max_length=30)
