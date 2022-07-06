from django.shortcuts import render, redirect
from django.contrib.auth   import logout
from django.contrib.auth.decorators import login_required
 
from preferances.models import Preferances
from django.contrib.auth.models import User 

@login_required(login_url='/login')
def dashboard(request):
    preferances = Preferances.objects.filter(user = request.user ).first()
    print(request.user) 
    print(preferances )
    return render(request, 'dashboard.html')

@login_required(login_url='/login')
def logout_fn(request):
    logout(request)
    return redirect('/')
