from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Events.urls", namespace = 'events')),
    path('reg/', include("Register.urls", namespace = 'register')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
