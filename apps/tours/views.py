from django.shortcuts import render
from apps.tours.models import Tour
from apps.settings.models import Setting

# Create your views here.
def tour_detail(request, id):
    home = Setting.objects.latest('id')
    tour = Tour.objects.get(id = id)
    context = {
        'home' : home,
        'tour' : tour,
    }
    return render(request, 'tour_detail.html', context)