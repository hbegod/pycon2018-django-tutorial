from django.db import models


class AstronomicalObjectScale(models.Model):
    """Масштаб в объемах вселенной."""

    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Масштабность объекта'
        verbose_name_plural = 'Масштабность объектав'


class ClassificationType(models.Model):
    """Тип классификации."""

    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Tип классификации'
        verbose_name_plural = 'Типы классификации'


class AstronomicalObjectType(models.Model):
    """Тип объекта в классификации."""
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Тип небесного тела'
        verbose_name_plural = 'Типы небесных тел'


class AstronomicalObjectGroup(models.Model):
    """Тип объектов."""

    asto_type = models.ForeignKey(
        'AstronomicalObjectType',
        blank=False, null=False,
        on_delete=models.CASCADE
    )
    classification = models.ForeignKey(
        'ClassificationType',
        blank=False, null=False,
        on_delete=models.CASCADE
    )
    scale = models.ForeignKey(
        'AstronomicalObjectScale',
        blank=False, null=False,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Астрономический объект'
        verbose_name_plural = 'Астрономические объекты'
