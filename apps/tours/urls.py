from django.urls import path 
from apps.tours.views import tour, tour_plan, search, tour_create,tour_update,post_share



urlpatterns = [
    path('tour/', tour, name = "tour"), 
    path('tour_plan/<int:id>', tour_plan, name = "tour_plan"), 
    path('search/', search, name = "search"),
    path('create/', tour_create, name = "tour_create"),
    path('update/<int:id>', tour_update, name = "tour_update"), 
    path('<post_id>/share', post_share, name='post_share'),

]

  