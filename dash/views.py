from django.shortcuts import render


def index(request):
    return render(request, 'testgraph.html', context={'text':'Hellow'})
    
