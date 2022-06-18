from django.contrib import admin
from apps.tours.models import Tour, Price, Benefits

# Register your models here.
admin.site.register(Tour)
admin.site.register(Price)
admin.site.register(Benefits)