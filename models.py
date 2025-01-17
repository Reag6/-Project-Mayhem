﻿"""
Definition of models.
"""

from email.mime import image
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib import admin
from django.utils import timezone
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User




class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")

    description = models.TextField(verbose_name="Краткое содержание")

    content = models.TextField(verbose_name="Полное содержание")

    posted = models.DateTimeField(default = datetime.now, db_index=True, verbose_name="Опубликована")

    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Автор")

    image = models.FileField(default = 'temp.jpg', verbose_name="Путь к картинке")


    # методы класса
    def get_absolute_url(self):  # метод возвращает строку с URL-адресом записи
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self):  # метод возвращает название, используемое для представления отдельных записей в адм. разделе
        return self.title

    # метаданные - вложенный в класс, который задает дополнительные параметры модели:
    class Meta:
        db_table = "Posts"  # имя таблицы для модели
        ordering = ["-posted"]  # порядок сортировки данных в модели ("-" означает убывание)
        verbose_name = "статья блога"  # имя, под которым модель будет отображаться в адм. разделе (для одной статьи блога)
        verbose_name_plural = "статьи блога"  # тоже для всех статей блога

# Регистрация модели в админке
admin.site.register(Blog)

class Comment(models.Model):

    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Дата комментария")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    post = models.ForeignKey('Blog', on_delete=models.CASCADE, verbose_name="Статья комментария")

    def __str__(self):

        return 'Комментарий %d %s к %s' % (self.id, self.author, self.post)

    class Meta:

        db_table = "Comment"

        ordering = ["-date"]

        verbose_name = "Комментарий к статье блога"

        verbose_name_plural = "Комментарии к статьям блога"

admin.site.register(Comment)

from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    master = models.CharField(max_length=100)
    services = models.CharField(max_length=255)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"




