# Fitness-Studio-Booking-API
A simple Booking API for a fictional fitness studio offering classes like Yoga, Zumba, and HIIT. Built using FastAPI with SQLite as in-memory storage and timezone support.

 # Features
 List Available Classes – View all upcoming fitness classes with details.

Book a Class – Book a spot in any class if slots are available.

View Bookings – Retrieve all bookings made using a specific email.

Timezone Support – Classes are managed in IST and dynamically adjusted to any timezone.

Validations & Error Handling – Prevents overbooking, validates inputs, and handles edge cases.

# Tech Stack
Framework: Django, Django REST Framework

Database: SQLite (default)

Timezone Handling: pytz, datetime

Others: Logging, Django Unit Tests


# instructions to clone
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness_booking

# create virtual environment
python -m venv venv
#  Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run migrations and seed data
python manage.py migrate
python manage.py loaddata seed_data.json  # Optional: preloaded class data

# start development server
python manage.py runserver

# go to API end point : GET /api/book/
Book the slots




