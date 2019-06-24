from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the report index.")


def trackers(request):
    return HttpResponse("You're looking at the list of trackers.")


def tracker_add(request):
    return HttpResponse("You're looking to add a tracker.")


def tracker_details(request, tracker_id):
    response = "You're looking at the details of tracker %s"
    return HttpResponse(response % tracker_id)


def records(request):
    return HttpResponse("You're looking at the list of trackers.")


def record_add(request):
    return HttpResponse("You're looking to add a record")


def record_details(request, record_id):
    response = "You're looking at the details of record %s"
    return HttpResponse(response % record_id)
