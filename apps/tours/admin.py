from django.contrib import admin
from apps.tours.models import Tour,Tour_plan,Tour_image,Discount,Comment,Like
# Register your models here.
# class Tour_imageAdmin(admin.TabularInline):
#     model = Tour_image
#     extra = 5

class TourAdmin(admin.ModelAdmin): 
    # inlines = [Tour_imageAdmin]
    list_display = ('name', 'price')
    search_fields = ('name', 'price')
    ordering = ('-price',)
    list_per_page = 10

admin.site.register(Tour,TourAdmin)
admin.site.register(Tour_plan)
admin.site.register(Discount)
admin.site.register(Comment) 
admin.site.register(Like)
admin.site.register(Tour_image)




 