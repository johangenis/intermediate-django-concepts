from django.contrib import admin
from django.urls import path

from core.views import login_view, register_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
]
