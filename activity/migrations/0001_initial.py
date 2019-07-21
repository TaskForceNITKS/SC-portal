# Generated by Django 2.2.2 on 2019-07-20 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('subtitle', models.CharField(max_length=120)),
                ('image', models.CharField(default='https://via.placeholder.com/800x400', max_length=200)),
                ('description', models.TextField()),
                ('section', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Technical Club'), (2, 'Cultural Club'), (3, 'Fest'), (4, 'Sports'), (None, 'Other')], null=True)),
            ],
        ),
    ]
