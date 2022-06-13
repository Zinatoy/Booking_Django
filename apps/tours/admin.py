from django.contrib import admin
from apps.tours.models import Tour,Tour_plan,Discount,Comment,Like
# Register your models here.
 

class TourAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price')
    search_fields = ('name', 'price')
    ordering = ('-price',)
    list_per_page = 10

admin.site.register(Tour,TourAdmin)
admin.site.register(Tour_plan)
admin.site.register(Discount)
admin.site.register(Comment) 
admin.site.register(Like)




 