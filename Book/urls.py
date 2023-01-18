from django.urls import path
from .views import myfunc, base, djangoform


urlpatterns = [
    path('addbook/', myfunc, name='books'),
    path('home/', base, name='base'),
    path('dform/', djangoform, name='dform')
]