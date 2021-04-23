from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'flights/index.html',{
    'flights':Flight.objects.all(),
    'baramati':Airport.objects.filter(city="baramati")
    } )


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, 'flights/flight.html',{
    'flight':flight,
    'passenger':flight.passenger.all()
    })
