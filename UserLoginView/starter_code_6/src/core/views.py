from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import UserRegisterForm

def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            auth_user = authenticate(username=user.username, password=password)
            login(request, auth_user)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, "register.html", context)