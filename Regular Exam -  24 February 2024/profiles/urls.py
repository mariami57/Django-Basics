from django.urls import path, include

from profiles.views import ProfileCreateView, ProfileDetailView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('profile/', include([
        path('create/', ProfileCreateView.as_view(), name='create-profile'),
        path('details/', ProfileDetailView.as_view(), name='details-profile'),
        path('edit/', ProfileEditView.as_view(), name='edit-profile'),
        path('delete/', ProfileDeleteView.as_view(), name='delete-profile'),
    ]))
]