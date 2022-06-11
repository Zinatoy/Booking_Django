from django.urls import path 
from apps.destinations.views import country, country_details



urlpatterns = [
    path('country/<int:id>', country, name = "country"), 
    path('country_details/', country_details, name = "country_details"), 

]