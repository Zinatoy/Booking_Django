from django.shortcuts import render, redirect, get_object_or_404
from apps.tours.models import Tour,Tour_plan,Comment,Like,Discount
from apps.settings.models import Settings
from apps.categories.models import Category
from django.db.models import Q
from apps.tours.forms import TourCreateForm, TourUpdateForm, EmailPostForm
from django.core.mail import send_mail
# Create your views here.

def tour_plan(request):
    home = Settings.objects.latest('id')
    tour = Tour.objects.all()
    category = Category.objects.all()

    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        message = request.POST.get('comment_message')
        comment = Comment.objects.create(message=message, tour=tour, user=request.user)
        return redirect('tour', tour.id)
    context = {
        'home': home,
        'tour' : tour,
        'category' : category,
    }
    return render(request, 'tour_plan.html', context)


def tour(request,id):
    home = Settings.objects.latest('id')
    tour= Tour.objects.get(id = id)
    random = Tour.objects.all().order_by('?')[:20]
    tour_plan = Tour_plan.objects.get(id=id)
    category = Category.objects.all().order_by('?')[:5]
    
    if 'like' in request.POST:
        try:
            like = Like.objects.get(user=request.user, tour=tour)
            like.delete()
        except:
            Like.objects.create(user=request.user, tour=tour)
    # if 'comment' in request.POST:
    #     id = request.POST.get('post_id')
    #     message = request.POST.get('comment_message')
    #     comment = Comment.objects.create(message=message, tour=tour, user=request.user)
    #     return redirect('tour', tour.id)

    context = {
        'home': home,
        'tour' : tour,
        'category' : category,
        'tour_plan' : tour_plan,
        'random' : random,
    }
    return render(request, 'tour_plan.html', context)
 
 
def search(request):
    tours = Tour.objects.all()
    qury_obj = request.GET.get('key')
    home = Settings.objects.latest('id')
    if qury_obj:
        tours = Tour.objects.filter(Q(title__icontains = qury_obj))
    context = {
        'home' : home, 
        'tours' : tours
    }
    return render(request, 'tour/search.html', context)

def tour_create(request):
    form = TourCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form' : form
    }
    return render(request, 'tour/create.html', context)

def tour_update(request, id):
    tour = Tour.objects.get(id = id)
    form = TourUpdateForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('tour/tour_plan', product.id)
    context = {
        'form' : form
    }
    return render(request, 'tour/update.html', context)

 

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Tour, id=post_id)
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'tour/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})