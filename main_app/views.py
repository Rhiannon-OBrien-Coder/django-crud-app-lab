from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coffee

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coffee_index(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffees/index.html', {'coffees': coffees})

def coffee_detail(request, cat_id):
    coffee = Coffee.objects.get(id=cat_id)
    return render(request, 'coffees/detail.html', {'coffee': coffee})

class CoffeeCreate(CreateView):
    model = Coffee
    fields = ['name', 'brand', 'description', 'rating']
    success_url = '/coffees/'

class CoffeeUpdate(UpdateView):
    model = Coffee
    fields = ['brand', 'description', 'rating']

class CoffeeDelete(DeleteView):
    model = Coffee
    success_url = '/coffees/'