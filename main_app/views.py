from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Show
from .forms import ServicesForm


# Create your views here.

class CarCreate(CreateView):
  model = Car
  fields = ['make', 'model', 'year']

class CarUpdate(UpdateView):
  model = Car
  fields = ['make', 'year']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

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
  shows_car_doesnt_have = Show.objects.exclude(id__in = car.shows.all().values_list('id'))  
  service_form = ServicesForm()
  return render(request, 'cars/detail.html', { 'car': car, 'service_form': service_form, 'shows': shows_car_doesnt_have })

def add_service(request, car_id):
  # create a ModelForm instance using the data in request.POST
  form = ServicesForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_service = form.save(commit=False)
    new_service.car_id = car_id
    new_service.save()
  return redirect('detail', car_id=car_id)

class ShowList(ListView):
  model = Show

class ShowDetail(DetailView):
  model = Show

class ShowCreate(CreateView):
  model = Show
  fields = '__all__'

class ShowUpdate(UpdateView):
  model = Show
  fields = ['name', 'location']

class ShowDelete(DeleteView):
  model = Show
  success_url = '/shows/'

def assoc_show(request, car_id, show_id):
  # Note that you can pass a toy's id instead of the whole object
  Car.objects.get(id=car_id).shows.add(show_id)
  return redirect('detail', car_id=car_id)