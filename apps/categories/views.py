from django.shortcuts import render
from apps.categories.models import Category 
from apps.settings.models import Settings
from apps.destinations.models import Country
from django.core.paginator import Paginator

# Create your views here.
def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    categories = Category.objects.all().order_by('?')[:5]
    home = Settings.objects.latest('-id')
    countries = Country.objects.all().order_by('-id')
    paginator = Paginator(categories, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category' : category,
        'coutries' : countries,
        'home' : home,
        'categories' : categories,
        'page_obj': page_obj,
    }
    return render(request, 'category_detail.html', context)