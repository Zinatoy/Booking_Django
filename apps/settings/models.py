from django.db import models

# Create your models here.

#home
class Settings(models.Model):
    title = models.CharField(max_length=250,verbose_name="Название", help_text="BookingKG")
    description = models.TextField(verbose_name="Описание")
    logo = models.ImageField(upload_to ='logo/',verbose_name="Логотип")
    phone = models.CharField(max_length=250,verbose_name="Телефон номер",help_text="0707070707")
    email = models.CharField(max_length=255,verbose_name="Электронная почта",help_text="example@gmail.com") 
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"


#partners
class Partners(models.Model): 
    link_partner = models.CharField(
        verbose_name="Ссылка на партнера", max_length=250, blank=True, null=True)
    image = models.ImageField(verbose_name="Фото",  upload_to="parners/")

    class Meta:
        verbose_name_plural = "Партнёры"
        verbose_name = "Партнёра"

    def __str__(self):
        return self.link_partner


#team
class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "team/")
    position = models.CharField(max_length=50)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команду"
        verbose_name_plural = "Команды"


#about_us
class About(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О компании "
        verbose_name_plural = "О компании"