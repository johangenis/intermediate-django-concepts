from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserLoginForm


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()
            auth_user = authenticate(username=user.username, password=password)
            login(request, auth_user)
            return redirect("/")
    context = {"form": form}
    return render(request, "register.html", context)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            return redirect("/")
    context = {"form": form}
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")
