from django.shortcuts import render

import subscription

 
def subscription(request):
    return render(request, 'subscription.html')