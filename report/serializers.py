from rest_framework import serializers
from .models import Tracker, Record, TrackerStatus, LocationMethod


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ("id", "animal_id", "status", "max_error_radius", "location_method")
        read_only_fields = ("id",)


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = (
            "id",
            "tracker",
            "timestamp",
            "geo_lat",
            "geo_long",
            "geo_error_radius",
            "geo_method",
        )
        read_only_fields = (
            "id",
            "tracker",
            "timestamp",
            "geo_lat",
            "geo_long",
            "geo_error_radius",
            "geo_method",
        )
