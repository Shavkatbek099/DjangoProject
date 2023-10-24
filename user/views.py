from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # email = request.POST["email"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga kirildi!!!")
            return redirect('home_page_dirs')
        else:
            messages.error(request, "Login yoki parol xato")
    return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    messages.info(request, "Siz tizimdan chiqdingiz.")
    return redirect("home_page_dirs")


def user_signup(request):
    if request.method == "POST":
        user = CustomUserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, "Account created successfully")
            return redirect('home_page_dirs')
        else:
            messages.error(request, "Username or Password is error.")
    else:
        user = CustomUserCreationForm()
        for i in user:
            if i.label == "Password":
                i.label = "Parol"
            elif i.label == "Password confirmation":
                i.label = "Parolni tasdiqlash"
    context = {'user': user}


    return render(request, "user/register.html", context)
