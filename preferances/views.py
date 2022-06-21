
from django.shortcuts import render
from preferances.forms import PreferancesForm

from preferances.models import Preferances

# Create your views here.

def preferances(request ):
    return render(request, 'preferances.html' )

def preferancesmodified(request):
    formm = PreferancesForm(request.POST )
    print(formm.data)    

    if formm.is_valid():
        print("Valid rcha")
        formm.save()
    context = {'PreferancesForm' : PreferancesForm}
 
    return render(request, 'preferancesmodified.html', context)