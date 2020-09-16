from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car


# Create your views here.
# Define the home view
def home(request):
  return render(request, 'home.html')

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

class CarCreate(CreateView):
  model = Car
  fields = '__all__'

class CarUpdate(UpdateView):
  model = Car
  fields = ['make', 'year']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'