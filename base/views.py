
from django.shortcuts import render

 

# Create your views here.
def home(request):
    return render(request, 'landing.html')

def login(request):
    return render(request, 'login.html')

 

def signup(request):
    return render(request, 'register.html') 

def registered(request):
    print(request)
    return(request, "register.html")        
