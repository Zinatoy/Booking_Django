from django.contrib import admin
from apps.settings.models import Setting, Partners, TourBooking, Facilities

# Register your models here.
admin.site.register(Setting)
admin.site.register(Partners)
admin.site.register(TourBooking)
admin.site.register(Facilities)