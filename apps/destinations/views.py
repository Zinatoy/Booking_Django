from django.shortcuts import render
from apps.destinations.models import Country, Country_details
from apps.settings.models import Settings
from apps.categories.models import Category
# Create your views here.

def country(request):
    country_categories = Category.objects.all()
    country = Country.objects.all()
    home = Settings.objects.latest('id')
    context = {
        'country_categories' : country_categories,
        'country' : country,
        'home' : home,
    }
    return render(request, 'destinations.html', context)

def country_details(request):
    home = Settings.objects.latest('id')
    country_details = Country_details.objects.all()
    context = {
        'home' : home,
        'country_details' : country_details,
    }

    return render(request, 'destinations-details.html', context)
