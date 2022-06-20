from django.shortcuts import render
from apps.settings.models import Setting,Facilities
from apps.tours.models import Tour, Benefits
from apps.staff.models import Staff

# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    tours = Tour.objects.all()
    staff = Staff.objects.all()
    benefits = Benefits.objects.all()
    facilities = Facilities.objects.all()
    context = {
        'home' : home,
        'tours' : tours,
        'staff' : staff,
        'benefits' : benefits,
        'facilities' : facilities,
    }
    return render(request, 'index.html', context)