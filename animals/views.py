from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateAnimal
from .models import Animal
# Create your views here.

def showAnimals(request):
    AnimalList = Animal.objects.all()
    context = {
        'Animals' : AnimalList
    }

    return render(request, 'animals/animals.html', context)
