# Generated by Django 4.0.5 on 2022-06-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0004_country_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='country_details',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('KZT', 'KZT'), ('KGS', 'KGS'), ('RUB', 'RUB')], default='USD', max_length=250),
        ),
    ]
