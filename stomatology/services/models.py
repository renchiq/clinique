from django.db import models


class Service(models.Model):
    name = models.CharField(verbose_name='Наименование услуги', max_length=200)
    price = models.CharField(verbose_name='Цена услуги', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['price']
