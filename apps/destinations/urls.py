from django.urls import path 
from apps.destinations.views import country, country_details



urlpatterns = [
    path('country/', country, name = "country"), 
    path('country_details/', country_details, name = "country_details"), 

]