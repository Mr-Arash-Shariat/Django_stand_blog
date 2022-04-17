from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def login_user(request):
    if request.user.is_authenticated == True:
        return redirect("home_page:home")

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page:home')

    return render(request, 'accounts/login.html', {})


def register_user(request):
    if request.user.is_authenticated == True:
        return redirect("home_page:home")
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Passwords is not match!!!")

        user = User.objects.create(email=email, username=username, password=password1)
        login(request, user)
        return redirect("home_page:home")

    return render(request, "accounts/register.html", {})


def logout_user(request):
    logout(request)
    return redirect('home_page:home')
