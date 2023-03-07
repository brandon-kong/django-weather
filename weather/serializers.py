from rest_framework import serializers
from .models import SavedLocation

class SavedLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedLocation
        fields = ['id', 'user', 'city', 'country', 'latitude', 'longitude']