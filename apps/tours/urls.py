from django.urls import path 
from apps.tours.views import tour_detail, tour_list, booking_system


urlpatterns = [
    path('tour/<int:id>', tour_detail, name = "tour_detail"),
    path('tour_list',tour_list, name = "tour_list" ),
    path('booking-system',booking_system, name = "booking-system")
]