from django.db import models


class Obj(models.Model):
    name = models.CharField('Название', max_length=15)
    is_deleted = models.BooleanField('На удаление', default=False)

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Spec(models.Model):
    link = models.ForeignKey(Obj, on_delete=models.CASCADE)
    is_actual = models.BooleanField('Актуальная запись', default=True)
    date = models.DateTimeField('Дата спецификацции')

    created_at = models.DateTimeField('Создано', auto_now_add=True)
    modify_at = models.DateTimeField('Изменено', auto_now=True)

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
