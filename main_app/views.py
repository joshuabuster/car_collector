from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

cars = [
  Car('Chevrolet', 'Chevelle', 1970),
  Car('Oldsmobile', '442', 1969),
  Car('Plymouth', 'Barracuda', 1972)
]

# Create your views here.
# Define the home view
def home(request):
  return HttpResponse('<h1>Home Page</h1>')

# Define the about view
def about(request):
  return render(request, 'about.html')

# Define the index view
def cars_index(request):
  return render(request, 'cars/index.html', {'cars': cars})