from django.shortcuts import render
from apps.settings.models import Settings,Partners,Team,About 
from apps.destinations.models import Country
from apps.tours.models import Tour,Tour_image

# Create your views here.

def index(request):
    home =  Settings.objects.latest('id')
    partners = Partners.objects.all()
    team = Team.objects.all()
    about = About.objects.all() 
    country = Country.objects.all() 
    tour = Tour.objects.all()
    tour_image = Tour_image.objects
    context = {
        'home' : home,
        'partners' : partners,
        'team' : team,
        'about' : about, 
        'country' : country, 
        'tour' : tour,

    }

    return render(request , 'index.html', context)

def about(request):
    about = About.objects.all() 
    home = Settings.objects.latest('id')
    partners = Partners.objects.all().order_by('-id') 
    team = Team.objects.all().order_by('-id')
    context = {
        'home':home, 
        'partners' : partners,
        'team' : team, 
        'about' : about
    }
    return render(request,'about.html',context)

