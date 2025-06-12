from django.urls import path, include

from traveler.views import TravelerCreateView, TravelerDeleteView, TravelerEditView, traveler_details_view

urlpatterns = [
    path("traveler/", include([
        path("create/", TravelerCreateView.as_view(), name="traveler_create"),

        path("edit/", TravelerEditView.as_view(), name="traveler_edit"),
        path("delete/", TravelerDeleteView.as_view(), name="traveler_delete"),

        path("details/", traveler_details_view, name="traveler_details"),

    ]))
]