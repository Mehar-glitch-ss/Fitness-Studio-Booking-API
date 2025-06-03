from .models import FitnessClass
from django.utils.timezone import make_aware
from datetime import datetime, timedelta

def seed_classes():
    classes = [
        ("Yoga", "Alice", datetime.now() + timedelta(days=1), 10),
        ("Zumba", "Bob", datetime.now() + timedelta(days=2), 15),
        ("HIIT", "Carol", datetime.now() + timedelta(days=3), 20),
    ]
    for name, instructor, dt, slots in classes:
        FitnessClass.objects.create(
            name=name,
            instructor=instructor,
            datetime_ist=make_aware(dt),
            total_slots=slots,
            available_slots=slots
        )
