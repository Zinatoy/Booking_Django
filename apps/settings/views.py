from django.shortcuts import render
from apps.settings.models import Setting
from apps.tours.models import Tour

# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    tours = Tour.objects.all()
    context = {
        'home' : home,
        'tours' : tours,
    }
    return render(request, 'index.html', context)