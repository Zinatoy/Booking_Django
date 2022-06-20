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

class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="tour_image", null=True)
    tour_image = models.ImageField(upload_to = "tour_image/", null = True, blank = True)

    class Meta:
        verbose_name = "Картинка тура"
        verbose_name_plural = "Картинки туров"

class Price(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="price_tour")
    date = models.DateField()
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.tour}"

    class Meta:
        verbose_name = "Цена тура"
        verbose_name_plural = "Цена туров"


class Benefits(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="benefits_tour")
    title = models.CharField(max_length=100)
    description = models.TextField()
    equipment = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"
