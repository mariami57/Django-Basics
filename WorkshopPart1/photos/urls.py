from django.urls import path, include

from photos import views

urlpatterns = [
    path("add/", views.add_photo_view, name='add_photo'),
    path("<int:pk>/", include([
        path("", views.details_photo_view, name="details_photo"),
        path("edit/", views.edit_photo_view, name="edit_photo"),
        path("delete/", views.photo_delete_view, name="delete_photo"),
    ]))
]