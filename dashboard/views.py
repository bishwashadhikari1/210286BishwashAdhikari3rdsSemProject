from django.shortcuts import render, redirect
from django.contrib.auth.models import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/user/login')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/user/login')
def logout_fn(request):
    logout(request)
    return redirect('/')
