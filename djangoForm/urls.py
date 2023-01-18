from django.urls import path
from .views import addbook, home

urlpatterns = [
    path('addbook/', addbook, name='addbook'),
    path('books/', home, name='home'),
]