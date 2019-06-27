from django.core import serializers
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from .models import Record, Tracker


def index(request):
    return HttpResponse("Hello, world. You're at the report index.")


def trackers(request):
    response_data = Tracker.objects.all()
    return HttpResponse(
        serializers.serialize("json", response_data), content_type="application/json"
    )


def tracker_add(request):
    return HttpResponse("You're looking to add a tracker.")


def tracker_details(request, tracker_id):
    response_data = Tracker.objects.filter(Q(pk=tracker_id))
    return HttpResponse(
        serializers.serialize("json", response_data), content_type="application/json"
    )


def records(request):
    response_data = Record.objects.all()
    return HttpResponse(
        serializers.serialize("json", response_data), content_type="application/json"
    )


def record_add(request):
    return HttpResponse("You're looking to add a record")


def record_details(request, record_id):
    response_data = Record.objects.filter(pk=record_id)
    return HttpResponse(
        serializers.serialize("json", response_data), content_type="application/json"
    )
