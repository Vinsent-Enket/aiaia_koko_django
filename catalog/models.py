from datetime import datetime

import django
from django.db import models
from django.utils import timezone
from pytils.translit import slugify

# Create your models here.
NULLABLE = {'blank': True, 'null': True}
now = django.utils.timezone.now


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.CharField(max_length=250, verbose_name='Описание категории')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('description',)


class Blog(models.Model):
    header = models.CharField(max_length=150, verbose_name='Заголовок поста')
    slug = models.CharField(max_length=150, verbose_name='Слаг', **NULLABLE, default=slugify(header))
    text = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='blog/', verbose_name='Превью', **NULLABLE)
    date_of_creation = models.DateField(verbose_name='Дата создания', default=now)
    is_published = models.BooleanField(verbose_name='Было опубликовано', default=True)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.header}'

    class Meta:
        verbose_name = 'пост'  # Настройка для наименования одного объекта
        verbose_name_plural = 'посты'  # Настройка для наименования набора объектов
        ordering = ('header', 'date_of_creation')


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название товара')
    description = models.CharField(max_length=250, verbose_name='Описание товара')
    images = models.ImageField(upload_to='product/', verbose_name='Картинка', **NULLABLE,
                               default='apu-upal-i-uronil-edu.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateField(verbose_name='Дата создания', default=now)
    date_of_change = models.DateField(verbose_name='Дата изменения', default=now)

    # posts = models.ManyToManyField(Blog, verbose_name='Отзывы о товаре', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'товары'  # Настройка для наименования набора объектов
        ordering = ('description',)
