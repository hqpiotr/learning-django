# Created on my own, in order to see sth when this address is clicked:
# /playground/hello --> call views.py (Hello World)

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello)
]