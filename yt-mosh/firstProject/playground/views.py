from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here. Playground: views.py
# Take request, send the response. Request handler. Action.
def say_hello(request):
    return HttpResponse('Hello World, playground::views.py.')