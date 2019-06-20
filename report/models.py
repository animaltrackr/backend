from django.db import models
from enum import Enum


class TrackerStatus(Enum):
    A = "Active"
    D = "Disabled"
    R = "Retired"
    U = "Unresponsive"
    X = "Unused"


# Create your models here.
class Tracker(models):
    animal_id: models.CharField(max_length=255)
    status: models.CharField(
        max_length=3, choices=[(tag, tag.value) for tag in TrackerStatus]
    )

    def __str__(self):
        return self.animal_id


class Record(models):
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE)
    timestamp = models.DateTimeField("date time recorded")
    geo__lat = models.DecimalField(max_digits=9, decimal_places=6)
    geo__long = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.tracker.animal_id} - {self.timestamp}"
