
from django.shortcuts import render

user_info=[
   { 'id':1,  'username':'kidwoo', 'password':'ilikewaffles'},
   { 'id':2, 'username':'woowasthat', 'password':'howisitliketodie'},
   { 'id':3, 'username':'popsmoke', 'password':'thewoo'}
]

# Create your views here.
def home(request):
    context = {'user_info' : user_info}
    return render(request,'base/home.html', context)

def users(request, pk):
    userss = None
    for i in user_info:
        if i['id']==int(pk):
            userss=i
    context={'user':userss}
    return render(request,'base/register.html', context)