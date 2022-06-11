from django.shortcuts import render
from apps.settings.models import Settings,Partners,Team,About

# Create your views here.

def index(request):
    home =  Settings.objects.latest('id')
    partners = Partners.objects.all()
    team = Team.objects.all()
    about = About.objects.all()
    context = {
        'home' : home,
        'partners' : partners,
        'team' : team,
        'about' : about,
    }

    return render(request , 'index.html', context)

