from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def display_data(request):
    data = '<marquee style = "color:red" direction = right> Welcome to learn Django and REST API by SANDESH H S</marquee>'
    return HttpResponse(data)