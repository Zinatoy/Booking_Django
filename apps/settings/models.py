from django.db import models

# Create your models here.


class Settings(models.Model):
    title = models.CharField(max_length=250,verbose_name="Название", help_text="BookingKG")
    description = models.TextField(verbose_name="Описание")
    logo = models.ImageField(upload_to ='logo/',verbose_name="Логотип")
    phone = models.CharField(max_length=250,verbose_name="Телефон номер",help_text="0707070707")
    email = models.CharField(max_length=255,verbose_name="Электронная почта",help_text="example@gmail.com") 

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"