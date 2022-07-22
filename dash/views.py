from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.core import session
from helpers.websocketcall import stopbot
import sqlite3, os
from preferances.models import Preferances


# @login_required(login_url='/login')
# def index(request):
#     # session(request.user.first_name,request.user.last_name)
#     event_triger()
#     return render(request, 'testgraph.html', context={'text':'5'})
    


@login_required
def dashboard(request, username):

    return render(request, 'testgraph.html', context={'text':'5','username':username})


@login_required
def static_dash(request, username):
    stopbot(session=session(request.user.first_name, request.user.last_name))
    pref = Preferances.objects.get(user_id = request.user.id)
    return render(request, 'dashboard.html', context={'text':5, 'username':username, 'preferances' : pref})

