from django.db import models

# Create your models here.
"""duct:
наименование,
описание,
изображение (превью),
категория,
цена за штуку,
дата создания,
дата последнего изменения.
"""
NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    """Category:
наименование,
описание."""
    name = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.CharField(max_length=250, verbose_name='Описание категории')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('description', )


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название товара')
    description = models.CharField(max_length=250, verbose_name='Описание товара')
    images = models.ImageField(upload_to='product/', verbose_name='Картинка', **NULLABLE)
    #category = models.CharField(max_length=150, verbose_name='Категория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateField(verbose_name='Дата создания ')
    date_of_change = models.DateField(verbose_name='Дата изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'товары'  # Настройка для наименования набора объектов
        ordering = ('description', )


