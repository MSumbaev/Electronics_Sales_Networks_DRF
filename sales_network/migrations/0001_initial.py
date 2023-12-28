# Generated by Django 5.0 on 2023-12-27 18:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('release_date', models.DateField(verbose_name='Дата выпуска')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='NetworkElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('element_type', models.CharField(choices=[('Factory', 'Завод'), ('Retail_network', 'Розничная сеть'), ('Individual_entrepreneur', 'Индивидуальный предприниматель')], max_length=100, verbose_name='Тип звена')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='email')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='Задолженность')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('suppliers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sales_network.networkelement', verbose_name='Поставщик')),
                ('products', models.ManyToManyField(to='sales_network.product', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'Звено сети',
                'verbose_name_plural': 'Звенья сети',
            },
        ),
    ]