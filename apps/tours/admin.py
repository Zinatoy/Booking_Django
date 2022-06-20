from django.contrib import admin
from apps.tours.models import Tour, Price, Benefits, TourImage

# Register your models here.
class TourImageAdmin(admin.TabularInline):
    model = TourImage
    extra = 6

class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageAdmin]
    list_per_page = 10

admin.site.register(Tour, TourAdmin)
admin.site.register(Price)
admin.site.register(Benefits)
admin.site.register(TourImage)