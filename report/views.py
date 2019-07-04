from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Record, Tracker
from .serializers import TrackerSerializer, RecordSerializer


def index(request):
    #  TODO: Render webpage with endpoint documentation
    return HttpResponse("Hello, world. You're at the report index.")


@csrf_exempt
def tracker_list(request):
    if request.method == "GET":
        trackers = Tracker.objects.all()
        serializer = TrackerSerializer(trackers, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TrackerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)


@csrf_exempt
def tracker_details(request, tracker_id):
    try:
        tracker = Tracker.objects.get(pk=tracker_id)
    except Tracker.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TrackerSerializer(tracker)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TrackerSerializer(tracker, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        tracker.delete()
        return HttpResponse(status=204)


@csrf_exempt
def record_list(request):
    if request.method == "GET":
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)


@csrf_exempt
def record_details(request, record_id):
    try:
        record = Record.objects.get(pk=record_id)
    except Record.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = RecordSerializer(record)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = RecordSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        record.delete()
        return HttpResponse(status=204)
