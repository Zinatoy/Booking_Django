from django.urls import path 
from apps.destinations.views import tour, tour_plan



urlpatterns = [
    path('tour/<int:id>', tour, name = "tour"), 
    path('tour_details/', tour_plan, name = "tour_plan"), 

]