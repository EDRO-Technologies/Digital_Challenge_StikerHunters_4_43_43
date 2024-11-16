from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Events.urls", namespace = 'events')),
    path('reg/', include("Register.urls", namespace = 'register')),
]
