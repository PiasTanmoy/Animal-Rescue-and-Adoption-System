from django import forms
from .models import Adoption

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ('name', 'contact_no', 'present_address', 'nid_no')