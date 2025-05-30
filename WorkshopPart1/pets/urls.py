from django.urls import path, include

from pets import views

urlpatterns = [
    path("add/", views.add_pet_view, name="add_pet"),
    path("<str:username>/pet/<slug:pet_slug>/", include([
        path("", views.details_pet_view, name="details_pet"),
        path("edit/", views.edit_pet_view, name="edit_pet"),
        path("delete/", views.delete_pet_view, name="delete_pet"),
    ]))
]