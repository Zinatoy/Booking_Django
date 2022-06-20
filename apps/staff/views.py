from django.shortcuts import render
from apps.staff.models import Staff

# Create your views here.
def staff(request):
    staff = Staff.objects.all()
    context = {
        'staff' : staff
    }
    return render(request , 'staff.html', context)
