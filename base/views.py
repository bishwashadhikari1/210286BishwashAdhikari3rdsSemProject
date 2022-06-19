
from django.shortcuts import render
from base.forms import RegisterForm

  

# Create your views here.
def home(request):
    return render(request, 'landing.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    context = {'RegisterForm' : RegisterForm}

    return render(request, 'preferances.html', context ) 

 

def signup(request):
    formm = RegisterForm(request.POST )
    print(formm.data)    

    if formm.is_valid():
        print("Valid rcha")
        formm.save()
    context = {'RegisterForm' : RegisterForm}
    return render(request, 'register.html', context ) 

   
