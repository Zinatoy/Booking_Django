from django.urls import path
from apps.staff.views import staff


urlpatterns = [
    path('staff/', staff, name = "staff"),
]