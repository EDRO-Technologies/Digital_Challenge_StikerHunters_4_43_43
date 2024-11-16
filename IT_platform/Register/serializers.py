from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["username", "name", "second_name",
                  "surname", "birth", "is_organizer",
                  "category", "special", "github",
                  "portfolio", "image"]