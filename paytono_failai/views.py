from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime
from .models import Reservation, AvailableSlot
from .forms import ReservationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    """Pagrindinis puslapis."""
    return render(request, "puslapio_failai/home.html")

def registration(request):
    """Registracijos funkcija."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registracija sėkminga! Sveiki prisijungę.")
            return redirect("paytono_failai:home")
        else:
            messages.error(request, "Klaida registruojantis. Patikrinkite duomenis.")
    else:
        form = UserCreationForm()
    
    return render(request, "puslapio_failai/registracija.html", {"form": form})

def booking(request):
    """Rezervacijos funkcija."""
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rezervacija sėkminga!")
            return redirect("paytono_failai:home")
        else:
            messages.error(request, "Rezervacijos nepavyko. Patikrinkite duomenis.")
    else:
        form = ReservationForm()
    
    return render(request, "puslapio_failai/reservation_form.html", {"form": form})

def get_available_slots(request):
    """
    AJAX funkcija, grąžinanti laisvus laikus rezervacijai pagal pasirinktą datą.
    
    URL parametras:
      - date: datos reikšmė formatu "YYYY-MM-DD"
    
    Jei vartotojas nėra administratorius, rodomi tik neužimti laikai.
    
    Grąžina JSON sąrašą objektų su laukais:
      - id: slot'o ID
      - slot_time: laikas formatu "HH:MM"
    """
    date_str = request.GET.get("date")
    if not date_str:
        return JsonResponse({"error": "Datos parametras yra privalomas."}, status=400)
    
    try:
        # Konvertuojame gautą datą iš "YYYY-MM-DD" į datetime objektą
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({"error": "Neteisingas datos formatas. Naudokite YYYY-MM-DD."}, status=400)
    
    try:
        # Filtruojame laisvus laikus pagal pasirinktą datą
        slots = AvailableSlot.objects.filter(slot_date=date_obj)
        
        # Jei vartotojas nėra administratorius, rodykite tik neužimtus laikus
        if not request.user.is_staff and not request.user.is_superuser:
            slots = slots.exclude(reservation__isnull=False)
        
        # Paruošiame JSON atsakymą
        slots_list = [
            {"id": slot.id, "slot_time": slot.slot_time.strftime("%H:%M")}
            for slot in slots
        ]
        return JsonResponse(slots_list, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
