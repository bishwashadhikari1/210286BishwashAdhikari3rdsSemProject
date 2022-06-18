
from django.shortcuts import render
from base.forms import RegisterForm

from base.models import User
 

# Create your views here.
def home(request):
    return render(request, 'landing.html')

def login(request):
    return render(request, 'login.html')

 

def signup(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'RegisterForm': RegisterForm}    
    return render(request, 'register.html', context) 

def registered(request):
    print(request)

    return(request, "register.html")        
