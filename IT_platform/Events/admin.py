from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple


admin.site.register(Event)
admin.site.register(Organizer)
admin.site.register(Category)
admin.site.register(Special)