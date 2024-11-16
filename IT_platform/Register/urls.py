from django.urls import path
from .views import *

app_name = "regiter"

urlpatterns = [
    path('', regitser, name="register"),
]
