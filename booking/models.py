from django.db import models

# Create your models here.

from django.db import models

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    datetime_ist = models.DateTimeField()
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} by {self.instructor}"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"
