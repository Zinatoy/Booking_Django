from django.contrib import admin
from apps.settings.models import Settings,Partners,Team,About,Benefits

# Register your models here.
admin.site.register(Settings) 
admin.site.register(Partners) 
admin.site.register(Team) 
admin.site.register(About) 
admin.site.register(Benefits)