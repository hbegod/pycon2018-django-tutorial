# Generated by Django 2.0.4 on 2018-12-17 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Название')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='На удаление')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_actual', models.BooleanField(default=True, verbose_name='Актуальная запись')),
                ('date', models.DateTimeField(verbose_name='Дата спецификацции')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('modify_at', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specobj.Obj')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
    ]
