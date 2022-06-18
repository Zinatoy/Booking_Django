from django.contrib import admin
from apps.settings.models import Setting, Partners, TourBooking

# Register your models here.
admin.site.register(Setting)
admin.site.register(Partners)
admin.site.register(TourBooking)