from django import forms
from .models import Normaluser

class RescueForm(forms.ModelForm):
    class Meta:
        model = Normaluser
        fields = ('name', 'phone_no', 'location')