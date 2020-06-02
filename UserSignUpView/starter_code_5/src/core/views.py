from django.shortcuts import render

from .forms import UserRegisterForm


def register_view(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
    context = {"form": form}
    return render(request, "register.html", context)
