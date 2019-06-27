from django.urls import path

from . import views

app_name = "report"
urlpatterns = [
    # ex: /report/
    path("", views.index, name="index"),
    # ex: /report/trackers
    path("trackers", views.trackers, name="trackers"),
    # ex: /report/trackers/add
    path("trackers/add", views.tracker_add, name="tracker add"),
    # ex: /report/trackers/<uuid>
    path("trackers/<uuid:tracker_id>", views.tracker_details, name="tracker details"),
    # ex: /report/records
    path("records", views.records, name="records"),
    # ex: /report/records/add
    path("records/add", views.record_add, name="record add"),
    # ex: /report/records/<uuid>
    path("records/<uuid:record_id>", views.record_details, name="record details"),
]
