from django.urls import path 
from apps.tours.views import tour, tour_plan



urlpatterns = [
    path('tour/', tour, name = "tour"), 
    path('tour_plan/', tour_plan, name = "tour_plan"), 

]