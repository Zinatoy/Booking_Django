from tabnanny import verbose
from django.db import models

# Create your models here.

#destinations
class Country(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'image/', verbose_name="Картинка")
  

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


#destinations-details
class Country_details(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'image_details/', verbose_name="Картинка")
    price = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country') 
    visa = models.CharField(max_length= 255)
    language = models.CharField(max_length=255)
    CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('KZT', 'KZT'),
        ('KGS', 'KGS'),
        ('RUB', 'RUB'),
    )
    area = models.IntegerField()


    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Информация о стране"
        verbose_name_plural = "Информация о странах"