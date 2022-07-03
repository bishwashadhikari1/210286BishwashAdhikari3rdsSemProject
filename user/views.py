from cmath import log
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login 

def login_page(request):
    if request.method == "POST":
        print(request.POST['password'])
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return redirect("/login")
    else:
        return render(request, "user/login-form.html")

def register_page(request):
    if request.method== "POST":
        User.objects.create_user(
            first_name = request.POST['apikey'],
            last_name = request.POST['apisecret'],
            username = request.POST['username'],
            password = request.POST['password'],
            email = request.POST['email'],
        )
        return redirect("/login")
    else:
        return render(request, "user/register-form.html")



