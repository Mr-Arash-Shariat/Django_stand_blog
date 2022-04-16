from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



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


def logout_user(request):
    logout(request)
    return redirect('home_page:home')
