from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer, BookingRequestSerializer
from django.utils.timezone import now

@api_view(['GET'])
def list_classes(request):
    classes = FitnessClass.objects.filter(available_slots__gt=0).order_by('datetime_ist')
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_class(request):
    serializer = BookingRequestSerializer(data=request.data)
    if serializer.is_valid():
        try:
            fitness_class = FitnessClass.objects.get(id=serializer.validated_data['class_id'])
            if fitness_class.available_slots <= 0:
                return Response({'error': 'No available slots'}, status=400)
            
            Booking.objects.create(
                fitness_class=fitness_class,
                client_name=serializer.validated_data['client_name'],
                client_email=serializer.validated_data['client_email']
            )
            fitness_class.available_slots -= 1
            fitness_class.save()

            return Response({'message': 'Booking successful'})
        except FitnessClass.DoesNotExist:
            return Response({'error': 'Class not found'}, status=404)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def view_bookings(request):
    email = request.query_params.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=400)

    bookings = Booking.objects.filter(client_email=email)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
