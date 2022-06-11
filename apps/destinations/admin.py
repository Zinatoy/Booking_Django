from django.contrib import admin
from apps.destinations.models import Country, Country_details
# Register your models here.

admin.site.register(Country)
admin.site.register(Country_details)