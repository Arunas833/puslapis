from django.db import models

class AvailableSlot(models.Model):
    slot_date = models.DateField(verbose_name="Data")
    slot_time = models.TimeField(verbose_name="Laikas")
    
    class Meta:
        unique_together = ('slot_date', 'slot_time')
        ordering = ['slot_date', 'slot_time']
    
    def __str__(self):
        return f"{self.slot_date} {self.slot_time}"

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    available_slot = models.ForeignKey(AvailableSlot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.available_slot}"

