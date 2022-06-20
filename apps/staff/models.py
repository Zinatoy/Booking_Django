from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length = 150)
    tel = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to = "staff-image/")
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cотрудник"
        verbose_name_plural = "Cотрудники"