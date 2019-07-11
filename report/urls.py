from django.urls import path

from . import views

app_name = "report"
urlpatterns = [
    # ex: /report/
    path("", views.index, name="index"),
    # ex: /report/trackers
    path("trackers", views.tracker_list),
    # ex: /report/trackers/<uuid>
    path("trackers/<uuid:tracker_id>", views.tracker_details),
    # ex: /report/points
    path("points", views.point_list),
    # ex: /report/points/<uuid>
    path("points/<uuid:point_id>", views.point_details),
]
