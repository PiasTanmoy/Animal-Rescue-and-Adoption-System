from django import forms
from django.forms import ModelForm
from .models import Animal

class CreateAnimal(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
