from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(verbose_name='Загловок', max_length=200)
    pub_date = models.DateField(verbose_name='Дата публикации', default=now())
    post_type_image = models.SmallIntegerField(verbose_name='Тип поста')
    description = models.CharField(verbose_name='Описание поста', max_length=500)
    content = models.TextField(verbose_name='Содержание поста')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pub_date']
