from django.shortcuts import render
from .forms import CreateUserForm, ProfileForm
from .models import Profile


def registrationPage(request):
    message = ""
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            message = "Registration Successful."
            form = ProfileForm()
    
    context = {
        'form' : form,
        'message' : message
    }
    
    return render(request, 'registration.html', context)


def profilePage(request):
    message = ""
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST)
        message = "Invalid input. Please try again!"

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            message = "Profile Created Successfully."
            form = ProfileForm()

    context = {
        'form' : form,
        'message' : message
    }
    
    return render(request, 'create_profile.html', context)


def showProfile(request):
    ProfileList = Profile.objects.all()

    context = {
        'Profiles' : ProfileList
    }

    return render(request, 'show_profile.html', context)
