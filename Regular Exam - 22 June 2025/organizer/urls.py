from django.urls import path, include

from organizer.views import OrganizerCreateView, OrganizerDetailView, OrganizerEditView, OrganizerDeleteView

urlpatterns = [
    path('organizer/', include([
        path('create/', OrganizerCreateView.as_view(), name='organizer_create'),
        path('details/', OrganizerDetailView.as_view(), name='organizer_details'),
        path('edit/', OrganizerEditView.as_view(), name='organizer_edit'),
        path('delete/', OrganizerDeleteView.as_view(), name='organizer_delete'),
    ]))
]