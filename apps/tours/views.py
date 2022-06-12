from django.shortcuts import render
from apps.tours.models import Tour,Tour_plan
from apps.settings.models import Settings
from apps.categories.models import Category
# Create your views here.

def tour(request):
    home = Settings.objects.latest('id')
    tour = Tour.objects.all()
    category = Category.objects.all()
    context = {
        'home': home,
        'tour' : tour,
        'category' : category,
    }
    return render(request, 'tour.html', context)


def tour_plan(request):
    home = Settings.objects.latest('id')
    tours_list = Tour.objects.all()
    tour_plan = Tour_plan.objects.all()
    category = Category.objects.all()
    context = {
        'home': home,
        'tour' : tour,
        'category' : category,
        'tour_plan' : tour_plan
    }
    return render(request, 'tour_plan.html', context)