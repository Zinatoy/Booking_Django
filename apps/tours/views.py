from django.shortcuts import render
from apps.tours.views import Tour,Tour_plan
from apps.settings.models import Settings
from apps.categories.models import Category
# Create your views here.

def tours_list(request):
    home = Settings.objects.latest('id')
    tour = Tour.objects.all()
    category = Category.objects.all()
    context = {
        'home': home,
        'tour' : tour,
        'category' : category,
    }
    return render(request, 'tours-list.html', context)


def tour_plan(request):
    home = Settings.objects.latest('id')
    tour = Tour.objects.all()
    plan = Tour_plan.objects.all()
    category = Category.objects.all()
    context = {
        'home': home,
        'tour' : tour,
        'category' : category,
        'plan' : plan
    }
    return render(request, 'tour-details.html', context)