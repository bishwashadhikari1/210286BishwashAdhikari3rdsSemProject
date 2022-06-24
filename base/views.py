
from django.shortcuts import render
from base.forms import RegisterForm

  

# Create your views here.
def home(request):
    return render(request, 'landing.html')

