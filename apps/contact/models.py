from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"