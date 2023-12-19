from django.db import models


class Table(models.Model):
    title = models.CharField('Назва статистики', max_length= 50)
    country = models.CharField('Країна', max_length= 50)
    year = models.CharField('Рік', max_length= 50)
    GDP = models.CharField('Значення', max_length= 50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Таблиці'
        verbose_name_plural = 'Данні'