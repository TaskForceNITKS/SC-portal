# Generated by Django 2.2.2 on 2019-06-20 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20190620_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='time_stamp',
        ),
        migrations.AddField(
            model_name='announcement',
            name='time_of_announcement',
            field=models.DateTimeField( verbose_name=datetime.datetime(2019, 6, 20, 16, 25, 46, 42185)),
            preserve_default=False,
        ),
    ]