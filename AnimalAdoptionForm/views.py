from django.shortcuts import render
from .forms import Adoption
from .forms import AdoptionForm

# Create your views here.
def showAdoptions(request):
    adoptionlist = Adoption.objects.all()
    context = {
        'adoptions' : adoptionlist
    }
    return render(request, 'AnimalAdoptionForm/adoptionlist.html',context)

def insertAdopter(request):
    form = AdoptionForm()
    if request.method == "POST":
        form = AdoptionForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        'form' : form
    }
    return render(request, 'AnimalAdoptionForm/insertAdopter.html', context)
