# Generated by Django 4.0.5 on 2022-06-11 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country_details',
            options={'verbose_name': 'Информация о стране', 'verbose_name_plural': 'Информация о странах'},
        ),
    ]
