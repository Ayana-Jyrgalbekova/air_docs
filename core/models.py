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


class DocumentNames(models.Model):
    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    doc_name = models.TextField()

    def __str__(self):
        return self.doc_name


class AllDocument(models.Model):
    class Meta:
        verbose_name = 'Все документы'
        verbose_name_plural = 'Все документы '

    plans = models.ForeignKey(DocumentNames, on_delete=CASCADE)
    category = models.ForeignKey(Categories, on_delete=CASCADE)
    when = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.when

