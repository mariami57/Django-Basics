from django.urls import path, include

from profiles.views import ProfileDetailView, ProfileDeleteView

urlpatterns=[
    path('profile/', include([
        path('details/', ProfileDetailView.as_view(), name='details-profile'),
        path('delete/', ProfileDeleteView.as_view(), name='delete-profile'),
    ]))
]