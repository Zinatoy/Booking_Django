from django.urls import path 
from apps.tours.views import tour, tour_plan, tour_create,tour_update,post_share

from . import views



urlpatterns = [
    path('tour/', tour, name = "tour"), 
    path('tour_plan/<str:id>', tour_plan, name = "tour_plan"), 
    path("search/", views.Search.as_view(), name='search'),
    path('create/', tour_create, name = "tour_create"),
    path('update/', tour_update, name = "tour_update"), 
    path('<post_id>/share', post_share, name='post_share'),

]

  