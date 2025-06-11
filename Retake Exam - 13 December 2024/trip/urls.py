from django.urls import path

from trip import views

urlpatterns = [
    path('', views.index, name='index'),
    path("all-trips/" , views.all_trips_view, name="all_trips"),
]