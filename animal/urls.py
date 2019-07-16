from django.urls import path

from . import views

app_name = "animal"
urlpatterns = [
    # ex: /animal/
    path("", views.index, name="index"),
    # ex: /animal/trackers
    path("trackers", views.tracker_list),
    # ex: /animal/trackers/<uuid>
    path("trackers/<uuid:tracker_id>", views.tracker_details),
    # ex: /animal/points
    path("points", views.point_list),
    # ex: /animal/points/<uuid>
    path("points/<uuid:point_id>", views.point_details),
]
