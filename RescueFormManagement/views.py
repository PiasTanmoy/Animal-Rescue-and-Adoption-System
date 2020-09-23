from django.shortcuts import render
from .models import Normaluser
from .forms import RescueForm

# Create your views here.
def showNormalusers(request):
    normaluserList = Normaluser.objects.all()
    context = {
        'normalusers' : normaluserList
    }
    return render(request, 'RescueFormManagement/normaluserlist.html', context)


def insertNormaluser(request):
    form = RescueForm()
    if request.method == "POST":
        form = RescueForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        'form' : form
    }
    return render(request, 'RescueFormManagement/insertNormaluser.html', context)
