from django.urls import path 
from apps.destinations.views import tours_list, tour_plan



urlpatterns = [
    path('tours_list/', tours_list, name = "tours_list"), 
    path('tour_plan/', tour_plan, name = "tour_plan"), 

]