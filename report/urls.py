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
    # ex: /report/records
    path("records", views.record_list),
    # ex: /report/records/<uuid>
    path("records/<uuid:record_id>", views.record_details),
]
