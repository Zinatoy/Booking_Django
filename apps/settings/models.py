from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to = "logo/")
    email = models.EmailField(max_length=255)
    tel = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class Partners(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "partners_image/")
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

class TourBooking(models.Model):
    date = models.DateField()
    people = models.PositiveBigIntegerField(default=0)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    tel = models.CharField(max_length=100)

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = "Бронь тура"
        verbose_name_plural = "Бронь туров"
