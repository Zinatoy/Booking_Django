from django.shortcuts import render
from apps.settings.models import Setting,Facilities,About,Partners
from apps.tours.models import Tour, Benefits,Price
from apps.staff.models import Staff
from django.db.models import Q
# Create your views here.
def index(request):
    search_query = request.GET.get('search', '')

    if search_query:
        tours = Tour.objects.filter(Q(title__icontains=search_query)| Q(description__icontains=search_query))
    else:
        tours = Tour.objects.all()

    home = Setting.objects.latest('id') 
    slide_tours = Tour.objects.all().order_by('-id')[:5]
    staff = Staff.objects.all()
    benefits = Benefits.objects.all()
    facilities = Facilities.objects.all()
    about = About.objects.all()
    partners = Partners.objects.all()
    price = Price.objects.all()

    
    context = {
        'home' : home,
        'slide_tours' : slide_tours,
        'tours' : tours,
        'staff' : staff,
        'benefits' : benefits,
        'facilities' : facilities,
        'about' : about,
        'partners' : partners,
        'price' : price,

    }
    return render(request, 'index.html', context)


def about(request):
    home = Setting.objects.latest('id')
    staff = Staff.objects.all()
    facilities = Facilities.objects.all()
    about = About.objects.all()
    partners = Partners.objects.all()
    context = {
        'home' : home,
        'staff' : staff,
        'facilities' : facilities,
        'about' : about,
        'partners' : partners,
    }
    return render(request, 'about.html', context)