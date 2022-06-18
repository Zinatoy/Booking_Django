from django.urls import path 
from apps.tours.views import tour_detail


urlpatterns = [
    path('tour/<int:id>', tour_detail, name = "tour_detail"),
]