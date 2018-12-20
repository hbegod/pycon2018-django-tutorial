from django.db import models
import


class DirectoryNomenclature(models.Model):
    nomenclature_name = models.CharField(max_length=30)
    manufacturers_name = models.OneToOneField(, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30)
