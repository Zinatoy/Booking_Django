from django.db import models
from apps.destinations.models import Country
from apps.categories.models import Category
from apps.users.models import User
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


 
#comments
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="comment" )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

#like
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes_user")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="likes_tour")

 

#discount
class Discount(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="discount")
    description = models.TextField()
    how_many_discount = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

