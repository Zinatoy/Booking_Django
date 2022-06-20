from django.shortcuts import render
from apps.tours.models import Tour,Price,Benefits
from apps.settings.models import Setting

# Create your views here.
def tour_detail(request, id):
    home = Setting.objects.latest('id')
    tour = Tour.objects.get(id = id)
    benefits = Benefits.objects.all()
    price = Price.objects.all()
    
    context = {
        'home' : home,
        'tour' : tour,
        'benefits' : benefits,
        'price' : price,

    }
    return render(request, 'tour_detail.html', context)