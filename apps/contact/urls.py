from django.urls import path 
from apps.contact.views import contact , thank_you

urlpatterns = [ 
    path('contact/', contact, name = "contact"),
    path('thank_you/', thank_you, name = "thank_you"), 
]