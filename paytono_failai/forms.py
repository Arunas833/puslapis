from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation, AvailableSlot

class ReservationForm(forms.ModelForm):
    slot_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Pasirinkite datą"
    )
    available_slot = forms.ModelChoiceField(
        queryset=AvailableSlot.objects.none(),
        label="Pasirinkite laiką",
        required=True
    )
    
    class Meta:
        model = Reservation
        # 'slot_date' nėra modelio laukas – jis naudojamas tik kaip filtras laiko pasirinkimui
        fields = ['name', 'email', 'slot_date', 'available_slot']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Jei formos POST duomenyse yra nurodyta data, užpildome laiko pasirinkimus
        if self.data.get('slot_date'):
            try:
                slot_date = self.data.get('slot_date')
                self.fields['available_slot'].queryset = AvailableSlot.objects.filter(slot_date=slot_date)
            except (ValueError, TypeError):
                self.fields['available_slot'].queryset = AvailableSlot.objects.none()
        elif self.instance.pk:
            self.fields['available_slot'].queryset = AvailableSlot.objects.filter(slot_date=self.instance.available_slot.slot_date)

    def clean(self):
        cleaned_data = super().clean()
        slot_date = cleaned_data.get("slot_date")
        available_slot = cleaned_data.get("available_slot")
        if available_slot and slot_date and available_slot.slot_date != slot_date:
            self.add_error('available_slot', "Pasirinkto laiko data neatitinka pasirinktos datos")
        return cleaned_data

    def save(self, commit=True):
        reservation = super().save(commit=False)
        if commit:
            reservation.save()
        return reservation


