# Generated by Django 3.2.12 on 2022-06-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='BookingKG', max_length=250, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип')),
                ('phone', models.CharField(help_text='0707070707', max_length=250, verbose_name='Телефон номер')),
                ('email', models.CharField(help_text='example@gmail.com', max_length=255, verbose_name='Электронная почта')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.RemoveField(
            model_name='aboutimage',
            name='about',
        ),
        migrations.DeleteModel(
            name='Setting',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='AboutImage',
        ),
    ]
