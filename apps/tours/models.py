from django.db import models

# Create your models here.
class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = "tour_image/")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"

class Price(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="price_tour")
    date = models.DateField()
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return self.tour


    class Meta:
        verbose_name = "Цена тура"
        verbose_name_plural = "Цена туров"


class Benefits(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="benefits_tour")
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"
