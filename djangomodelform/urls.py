from django.urls import path
from .views import bookthap, base

urlpatterns = [
    path('bookthap/', bookthap, name='bookthap'),
    path('base/', base, name='base')
]