import datetime
from json import dumps

import sqlite3, os
from django.shortcuts import render, redirect
from django.contrib.auth   import logout
from django.contrib.auth.decorators import login_required
from core.core import session, bsm
 
from preferances.models import Preferances
from django.contrib.auth.models import User 

# @login_required(login_url='/login')
# def dashboard(request):
#     a = session(request.user.first_name, request.user.last_name)
#     # bm = bsm(a)
#     try:
#         db = sqlite3.connect('realtime.db')
#         c = db.cursor()
#         datapll = c.execute("SELECT * FROM pnl")

#         data = datapll.fetchall()

#         labels = [row[0] for row in data]
#         values = [row[1] for row in data]
#         data = {
#             'pnl':values,
#             'label':labels
#         }
#     except:
#         data={}
#     preferances = Preferances.objects.filter(user = request.user).first()
#     print(preferances )
#     return render(request, 'dashboard.html', {'data':dumps(data)})

@login_required(login_url='/login')
def logout_fn(request):
    logout(request)
    return redirect('/')

# @login_required(login_url='/login')
# def dbrebase(request):
#     try:
#         os.remove('orders.db')
#     except:
#         print('no db yet')
#     db = sqlite3.connect('orders.db')
#     c = db.cursor()
#     c.execute(
#         """CREATE TABLE pnl(
#             time integer,
#             pnl float
#         )"""
#     )
#     db.commit()
#     db.close()

#     return redirect('/dashboard')

# @login_required(login_url='/login')
# def refresh(request):
#     a = session(request.user.first_name, request.user.last_name)
#     db = sqlite3.connect('realtime.db')
#     c = db.cursor()
#     b = a.futures_position_information()
#     upnl = 0
#     notion = 0
#     timee = 0
#     timey=0
#     for a in b:
#         if a['notional'] != "0":
#             notion += float(a['notional'])
#             upnl += float(a['unRealizedProfit'])
#             timee = datetime.datetime.now()
#             timey = int(timee.strftime("%Y%m%d%H%M%S"))

#     c.execute(
#     "INSERT INTO pnl VALUES(:time, :pnl)",{
#         "time": timey,
#         "pnl": upnl
#     }
#     )
#     db.commit()

#     return redirect('/dashboard')