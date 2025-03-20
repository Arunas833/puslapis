from django.contrib import admin
from .models import AvailableSlot, Reservation

@admin.register(AvailableSlot)
class AvailableSlotAdmin(admin.ModelAdmin):
    list_display = ('slot_date', 'slot_time')
    list_filter = ('slot_date',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'available_slot', 'created_at')
    list_filter = ('available_slot__slot_date',)

