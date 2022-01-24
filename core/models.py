from datetime import date

from django.contrib import messages
from django.db import models
from django.db.models import CASCADE


class Client(models.Model):
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    fio = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.fio


class Categories(models.Model):
    class Meta:
        verbose_name = 'Разделения'
        verbose_name_plural = 'Разделении'

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Documents(models.Model):
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    text = models.TextField(verbose_name='Текст')
    date = models.DateField(verbose_name='Дата выписки предписания')
    date_answer = models.DateField(verbose_name='Дата исполнения')
    fio = models.ForeignKey(Client, on_delete=CASCADE, verbose_name='Выполнил(а)')
    category = models.ForeignKey(Categories, on_delete=CASCADE, verbose_name='Предприятие(служба)')

    def __str__(self):
        return self.text

    @property
    def is_past_due(self):
        return date.today() == self.date_answer
