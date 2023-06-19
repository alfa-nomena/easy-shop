from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect



urlpatterns = [
    path('admin/', admin.site.urls),
    path("shop", include("shop.urls")),
    path('', lambda x: redirect("shop:home"))
]
