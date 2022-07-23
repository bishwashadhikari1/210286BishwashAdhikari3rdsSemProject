from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login
from django.contrib.auth.decorators import login_required
from sqlalchemy import true
from core.core import session
from preferances.models import Preferances
from subscription.models import Subscription 

def login_page(request):
    error=0

    if request.method == "POST":
        print(request.POST['password'])
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            return redirect(f"/dashboard/{user.username}")

        else:
            error = 1
            print(error)
            return render(request, "user/login-form.html", {'error':error})
    else:
        return render(request, "user/login-form.html")

def register_page(request):
    if request.method== "POST":
        try:
            session(request.POST['apikey'], request.POST['apisecret'])
            api_valid = true
        except:
            api_valid = False
            return redirect("/login")

        User.objects.create_user(
            first_name = request.POST['apikey'],
            last_name = request.POST['apisecret'],
            username = request.POST['username'],
            password = request.POST['password'],
            email = request.POST['email'],
        )
        userr = User.objects.get(username = request.POST['username'])

        pref = Preferances(user= userr )
        pref.save()    
        subs = Subscription(owner = userr)
        subs.save()
        
        return redirect("/login")
    else:
        return render(request, "user/register-form.html")


@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == "POST":
        ewwser = User.objects.get(username = request.user.username)
        ewwser.first_name = request.POST['apikey']
        ewwser.last_name = request.POST['apisecret']
        ewwser.email = request.POST['email']
        ewwser.save()
    return render(request, 'profileedit.html')

@login_required
def delete_user(request):
    youser  = User.objects.get(username = request.user.username)
    youser.delete()
    return redirect('/signup')