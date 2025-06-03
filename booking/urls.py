from django.urls import path
from . import views

urlpatterns = [
    path('classes/', views.list_classes, name='list-classes'),
    path('book/', views.book_class, name='book-class'),
    path('bookings/', views.view_bookings, name='view-bookings'),
]
