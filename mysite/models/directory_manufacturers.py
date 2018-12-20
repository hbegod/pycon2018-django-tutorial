from django.db import models


class DirectoryManufacturers(models.Model):
    name = models.CharField(max_length=30)
