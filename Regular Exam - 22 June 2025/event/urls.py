from django.urls import path, include

from event.views import EventsView, EventCreateView, EventDetailView, EventEditView, EventDeleteView

urlpatterns=[
    path('events/', include([
        path('', EventsView.as_view(), name='events'),
        path('create/', EventCreateView.as_view(), name='create-event'),
        path('<event_pk>/', include([
            path('details/', EventDetailView.as_view(), name='details-event'),
            path('edit/', EventEditView.as_view(), name='edit-event'),

            path('delete/', EventDeleteView.as_view(), name='delete-event'),
        ])),
    ]))
]