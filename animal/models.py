import uuid

from django.db import models
from django.utils import timezone
from enum import Enum
import datetime


class TrackerStatus(Enum):
    A = "Active"
    D = "Disabled"
    R = "Retired"
    U = "Unresponsive"
    X = "Unused"


class LocationMethod(Enum):
    G = "GPS"
    L = "LTE"
    B = "GPS+LTE"


# Create your models here.
class Tracker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(
        max_length=3, choices=[(tag.name, tag.value) for tag in TrackerStatus]
    )
    max_error_radius = models.DecimalField(max_digits=5, decimal_places=1)
    location_method = models.CharField(
        max_length=3,
        choices=[(tag.name, tag.value) for tag in LocationMethod],
        default=LocationMethod.B.name,
    )

    def __str__(self):
        return self.animal_id


class Point(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE)
    timestamp = models.DateTimeField("date time recorded")
    geo_lat = models.DecimalField(max_digits=9, decimal_places=6)
    geo_long = models.DecimalField(max_digits=9, decimal_places=6)
    geo_error_radius = models.DecimalField(max_digits=5, decimal_places=1)
    geo_method = models.CharField(
        max_length=3,
        choices=[(tag.name, tag.value) for tag in LocationMethod],
        default=LocationMethod.L.name,
    )

    def __str__(self):
        return f"{self.tracker.animal_id} - {self.timestamp}"

    def is_recent(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
