from django.urls import path
from .views import home, booking, get_available_slots, registration

app_name = "paytono_failai"  

urlpatterns = [
    path("", home, name="home"),  # Pagrindinis puslapis
    path("registracija/", registration, name="registracija"),  # Registracija
    path("rezervacija/", booking, name="booking"),  # Rezervacija
    path("get_available_slots/", get_available_slots, name="get_available_slots"),  # Laikų gavimas AJAX
]
