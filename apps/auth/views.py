from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user

@unauthenticated_user
def index(request):
    return render(request, "login.html")

def login_user(request):
    if request.method != "POST":
        return HttpResponse("Bad request method")
    
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)
    if not user:
        return HttpResponse("not a user lol")

    login(request, user)
    return redirect("/vote")

def logout_user(request):
    logout(request)
   
    return redirect("/")
