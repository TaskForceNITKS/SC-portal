# Generated by Django 2.2.2 on 2019-06-26 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0035_auto_20190624_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('the_file', models.FileField(blank=True, null=True, upload_to='mainapp.DocumentModel/bytes/filename/mimetype')),
            ],
        ),
        migrations.AlterField(
            model_name='announcement',
            name='time_of_announcement',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 26, 11, 8, 33, 787523)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_of_meeting',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 26, 11, 8, 33, 788064)),
        ),
    ]