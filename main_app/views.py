from django.shortcuts import render
from .models import Car
# Add the following import
from django.http import HttpResponse

# Create your views here.
# Define the home view
def home(request):
  return HttpResponse('<h1>Home Page</h1>')

# Define the about view
def about(request):
  return render(request, 'about.html')

# Define the index view
def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', {'cars': cars})

#  Define the details view
def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  return render(request, 'cars/detail.html', { 'car': car })