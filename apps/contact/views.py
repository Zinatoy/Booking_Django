from django.shortcuts import render
from apps.contact.models import Contact
from apps.contact.forms import ContactForm
# Create your views here. 

def contact(request):
    # home = Home.objects.latest('id')
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            contact = form.save()
            return redirect('thank_you')
   
    return render(request, 'contact.html', locals())

def thank_you(request):
    return render(request, 'thank_you.html')