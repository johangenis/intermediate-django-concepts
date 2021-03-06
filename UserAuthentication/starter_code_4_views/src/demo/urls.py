from django.contrib import admin
from django.urls import path

from core.views import register_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register", register_view, name="register"),
]
