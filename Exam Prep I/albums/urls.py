from django.urls import path, include

from albums.views import CreateAlbumView, AlbumDetailView, AlbumEditView, AlbumDeleteView

urlpatterns = [
    path('album/', include([
        path('add/', CreateAlbumView.as_view(), name='add-album'),
        path('<int:id>/', include([
            path('details/', AlbumDetailView.as_view(), name='details-album'),
            path('edit/', AlbumEditView.as_view(), name='edit-album'),
            path('delete/', AlbumDeleteView.as_view(), name='delete-album'),
        ]))
    ]))
]