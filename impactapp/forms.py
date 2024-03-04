from django import forms
from .models import contact,product



class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'

class productform(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'        