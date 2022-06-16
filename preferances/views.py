from django.shortcuts import render

# Create your views here.

def preferances(request ):
    return render(request, 'preferances.html' )