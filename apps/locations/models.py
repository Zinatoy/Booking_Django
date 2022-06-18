from django.db import models

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = "location_image/")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"