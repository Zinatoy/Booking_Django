# Generated by Django 4.0.5 on 2022-06-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_like_discount_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour_additional_images')),
            ],
            options={
                'verbose_name': 'Картинка с тура ',
                'verbose_name_plural': 'Картинки с тура',
            },
        ),
    ]
