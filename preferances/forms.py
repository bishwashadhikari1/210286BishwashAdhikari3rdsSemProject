from django import forms
from preferances.models import Preferances

class PreferancesForm(forms.ModelForm):
    class Meta:
        model  =  Preferances
        fields="__all__"