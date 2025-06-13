from django.urls import path, include

from trip import views
from trip.views import TripCreateView, TripEditView, TripDeleteView

urlpatterns = [
    path("", views.index, name="index"),
    path("all-trips/" , views.all_trips_view, name="all_trips"),

    path("trips/", include([
        path("create/", TripCreateView.as_view(), name="trip_create"),
        path("<int:pk>/", include([
            path("edit/", TripEditView.as_view(), name="trip_edit"),
            path("delete/", TripDeleteView.as_view(), name="trip_delete"),
            path("details/", views.trip_details, name="trip_details"),
        ]))
    ])),

]