from django.db import models
from django.utils import timezone


class MedicalCard(models.Model):
    number = models.CharField(verbose_name='Номер медкарты',
                              primary_key=True,
                              max_length=8,
                              db_index=True)
    started_date = models.DateField(verbose_name='Дата заведения медкарты',
                                    default=timezone.now)

    def __str__(self):
        return '№{0}'.format(self.number)

    class Meta:
        ordering = ['started_date']


class Record(models.Model):
    medical_card = models.ForeignKey(MedicalCard, on_delete=models.CASCADE)
    record_date = models.DateField(verbose_name='Дата внесения записи',
                                   default=timezone.now)
    visit_date = models.DateField(verbose_name='Дата посещения',
                                  default=timezone.now)
    title = models.CharField(verbose_name='Заголовок записи',
                             max_length=100)
    content = models.TextField(verbose_name='Содержание записи',
                               max_length=1000)

    def __str__(self):
        return '{0} {1}'.format(self.record_date, self.title)

    class Meta:
        ordering = ['record_date']
