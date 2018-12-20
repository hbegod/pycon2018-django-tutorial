from django.db import models


class DirectoryManufacturers(models.Model):
    manufacturers_name = models.CharField(max_length=30)
