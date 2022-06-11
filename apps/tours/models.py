from django.db import models
from apps.destinations.models import Country
# Create your models here.

#tours-list
class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='tour_image/')
    price = models.IntegerField()
    days = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank = True ,related_name='tour_country')
    rating = models.IntegerField()

    def __str__(self):
        return(self.name)

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


#tour-details
class Tour_plan(models.Model):
    which_day = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return(self.which_day)

    class Meta:
        verbose_name = "План тура"
        verbose_name_plural = "План туров"




