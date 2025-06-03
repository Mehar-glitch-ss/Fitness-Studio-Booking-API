from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer, BookingRequestSerializer

@api_view(['GET'])
def list_classes(request):
    """List all available classes with slots."""
    classes = FitnessClass.objects.filter(available_slots__gt=0).order_by('datetime_ist')
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def book_class(request):
    if request.method == 'GET':
        return Response({
            "info": "Send a POST request with 'class_id', 'client_name', and 'client_email' to book a class."
        })

    if request.method == 'POST':
        serializer = BookingRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:
                fitness_class = FitnessClass.objects.get(id=serializer.validated_data['class_id'])
                
                if fitness_class.available_slots <= 0:
                    return Response({'error': 'No available slots'}, status=status.HTTP_400_BAD_REQUEST)

                # Create booking
                Booking.objects.create(
                    fitness_class=fitness_class,
                    client_name=serializer.validated_data['client_name'],
                    client_email=serializer.validated_data['client_email']
                )

                # Update available slots
                fitness_class.available_slots -= 1
                fitness_class.save()

                return Response({'message': 'Booking successful'}, status=status.HTTP_201_CREATED)
            except FitnessClass.DoesNotExist:
                return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_bookings(request):
    """View bookings by client email (GET /bookings/?email=...)"""
    email = request.query_params.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

    bookings = Booking.objects.filter(client_email=email)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
