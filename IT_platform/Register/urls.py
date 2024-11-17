from django.urls import path, re_path, include
from .views import *

app_name = "register"

urlpatterns = [
    path('', regitser, name="register"),
    re_path(r'^auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls')),
]
