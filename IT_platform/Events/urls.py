from django.urls import path
from .views import *

app_name = "event"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('eventlist/', EventAPIList.as_view(), name="events"),
    path('eventcreate/', EventAPICreate.as_view(), name="events"),
    path('eventupdate/<int:pk>', EventAPIUpdate.as_view(), name="events"),
    path('eventdelete/<int:pk>', EventAPIDelete.as_view(), name="events"),
    path('eventfilter', EventFilter.as_view(), name="events"),
]
