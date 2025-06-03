from rest_framework import serializers
from .models import FitnessClass, Booking

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'instructor', 'datetime_ist', 'available_slots']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'fitness_class', 'client_name', 'client_email', 'booking_time']

class BookingRequestSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    client_name = serializers.CharField(max_length=100)
    client_email = serializers.EmailField()
