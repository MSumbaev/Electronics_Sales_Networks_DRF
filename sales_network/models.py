from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выпуска')

    def __str__(self):
        return f'{self.title} / {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class NetworkElement(models.Model):
    CHOICES_TYPE = [
        ('Factory', 'Завод'),
        ('Retail_network', 'Розничная сеть'),
        ('Individual_entrepreneur', 'Индивидуальный предприниматель')
    ]

    title = models.CharField(max_length=100, verbose_name='Название')
    element_type = models.CharField(max_length=100, choices=CHOICES_TYPE, verbose_name='Тип звена')

    email = models.CharField(max_length=100, unique=True, verbose_name='email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    products = models.ManyToManyField(Product, verbose_name='Продукты')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name='Задолженность')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}({self.email}) / {self.element_type}'

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'
