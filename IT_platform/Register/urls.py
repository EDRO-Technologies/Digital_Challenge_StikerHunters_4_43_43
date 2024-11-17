from django.urls import path, re_path, include
from .views import *

app_name = "register"

urlpatterns = [
    path('', ProfileAPICreate.as_view(), name="register"),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('success/', ProfileAPIList.as_view()),

]
