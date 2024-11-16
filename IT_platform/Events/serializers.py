from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "category", "special",
                  "place", "description", "date",
                  "organizer", "partners", "image"]

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ["title", "contact", "description", "image"]