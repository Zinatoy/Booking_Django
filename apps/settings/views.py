from django.shortcuts import render
from apps.settings.models import Settings

# Create your views here.

def index(request):
    home =  Settings.objects.latest('id')
    context = {
        'home' : home
    }

    return render(request , 'index.html', context)

