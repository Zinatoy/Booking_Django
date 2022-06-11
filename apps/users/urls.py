from django.urls import path 
from apps.users.views import register, login, user_profile, update_profile, delete_profile


urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', login, name = "login"),
    path('user/<int:id>', user_profile, name = "user_profile"),
    path('user/update/<int:id>', update_profile, name = "update_profile"),
    path('user/delete/<int:id>', delete_profile, name = "delete_profile"),
]