# Generated by Django 3.1.4 on 2020-12-11 14:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201211_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 11, 14, 48, 9, 60290, tzinfo=utc), verbose_name='Дата публикации'),
        ),
    ]
