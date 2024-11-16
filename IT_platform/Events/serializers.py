from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "category", "special",
                  "place", "description", "date",
                  "organizer", "partners", "image"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["username", "name", "second_name",
                  "surname", "birth", "is_organizer",
                  "category", "special", "github",
                  "portfolio", "image"]

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ["title", "contact", "description", "image"]