from django.shortcuts import render, redirect, get_object_or_404
from apps.tours.models import Tour,Tour_plan,Comment,Like,Discount
from apps.settings.models import Settings
from apps.categories.models import Category
from django.db.models import Q
from apps.tours.forms import TourCreateForm, TourUpdateForm, EmailPostForm
from django.core.mail import send_mail
from django.views.generic import ListView
# Create your views here.

def tour(request):
    home = Settings.objects.latest('id')
    tour = Tour.objects.all()
    category = Category.objects.all()
    plan = Tour_plan.objects.all()

    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        message = request.POST.get('comment_message')
        comment = Comment.objects.create(message=message, tour=tour, user=request.user)
        return redirect('tour', tour.id)
    context = {
        'home': home,
        'tour' : tour,
        'category' : category,
        'plan' : plan ,
    }
    return render(request, 'tour.html', context)


def tour_plan(request,id):
    home = Settings.objects.latest('id')
    tour= Tour.objects.all()
    random = Tour.objects.all().order_by('?')[:20]
    tour_plan = Tour_plan.objects.all()
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
 
 
class Search(ListView):
     
    paginate_by = 3

    def get_queryset(self):
        return Tour.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


class TourCountry: 

    def get_tour(self):
        return Tour.objects.all()

    def get_country(self):
        return Country.objects.filter(draft=False).values("title")

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