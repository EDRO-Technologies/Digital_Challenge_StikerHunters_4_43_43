from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'event', EventViewSet)

app_name = "event"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('api/', include(router.urls), name="view"),
]
