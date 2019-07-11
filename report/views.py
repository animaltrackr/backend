from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Point, Tracker
from .serializers import TrackerSerializer, PointSerializer


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
def point_list(request):
    if request.method == "GET":
        points = Point.objects.all()
        serializer = PointSerializer(points, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PointSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)


@csrf_exempt
def point_details(request, point_id):
    try:
        point = Point.objects.get(pk=point_id)
    except Point.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = PointSerializer(point)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        # points should be immutable
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        point.delete()
        return HttpResponse(status=204)
