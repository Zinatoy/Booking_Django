from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')  
        username = request.POST.get('username')
        profile_image = request.FILES.get('profile_image')
        email = request.POST.get('email') 
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                user = User.objects.create( username = username, name = name, surname = surname,  email = email, profile_image = profile_image)
                user.set_password(password1)
                user.save()
                return redirect('index')
            except:
                messages.error(request, 'Неправильные данные')
        else:
            messages.error(request, 'Пароли отличаются')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        except:
            messages.error("Неправильный логин или пароль")
       
    return render(request, 'login.html')