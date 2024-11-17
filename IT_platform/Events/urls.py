from django.urls import path
from .views import *

app_name = "event"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('test/', test, name="test"),
    path('eventlist/', EventAPIList.as_view(), name="events"),
    path('eventcreate/', EventAPICreate.as_view(), name="events"),
    path('eventupdate/<int:pk>', EventAPIUpdate.as_view(), name="events"),
    path('eventdelete/<int:pk>', EventAPIDelete.as_view(), name="events"),
]
