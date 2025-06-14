from django.urls import path, include

from author.views import AuthorCreate, AuthorDetails, AuthorEdit, AuthorDelete

urlpatterns=[
    path('author/', include([
        path('create/', AuthorCreate.as_view(), name='author-create'),
        path('details/', AuthorDetails.as_view(), name='author-details'),
        path('edit/', AuthorEdit.as_view(), name='author-edit'),
        path('delete/', AuthorDelete.as_view(), name='author-delete'),
    ]))
]