# Generated by Django 3.2.4 on 2021-08-16 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mm',
            options={'ordering': ['-published'], 'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]
