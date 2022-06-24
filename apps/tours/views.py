from django.shortcuts import render,redirect
from apps.tours.models import Tour,Price,Benefits,Comment
from apps.settings.models import Setting


# Create your views here.
def tour_detail(request, id):
    home = Setting.objects.latest('id')
    random_tours = Tour.objects.all().order_by('?')[:20]
    tour = Tour.objects.get(id = id)
    benefits = Benefits.objects.all()
    price = Price.objects.all()
    
    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        message = request.POST.get('comment_message')
        comment = Comment.objects.create(message=message, tour=tour, user=request.user)
        return redirect('tour_detail', tour.id)

    context = {
        'home' : home,
        'random_tours' : random_tours,
        'tour' : tour,
        'benefits' : benefits,
        'price' : price,

    }
    return render(request, 'tour_detail.html', context)

def tour_list(request): 
    tour = Tour.objects.all()
    benefits = Benefits.objects.all()
    price = Price.objects.all()
    context = {
        'tour' : tour,
        'benefits' : benefits,
        'price' : price,
    }
    return render(request, 'tour_list.html', context)