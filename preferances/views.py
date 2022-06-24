
from django.shortcuts import render
from preferances.forms import PreferancesForm
from django.contrib.auth.decorators import login_required

from preferances.models import Preferances

# Create your views here.

@login_required(login_url='/user/login')
def preferances(request ):
    return render(request, 'preferances.html' )


@login_required(login_url='/user/login')
def preferancesmodified(request):
    formm = PreferancesForm(request.POST )
    print(formm.data)    

    if formm.is_valid():
        print("Valid rcha")
        formm.save()
    context = {'PreferancesForm' : PreferancesForm}
 
    return render(request, 'preferancesmodified.html', context)