from django.urls import path, include

from author.views import CreateAuthor, DetailsAuthor, EditAuthor, DeleteAuthor

urlpatterns=[
    path('profile/', include([
        path('create/', CreateAuthor.as_view(), name='create-author' ),
        path('details/', DetailsAuthor.as_view(), name='detail-author' ),
        path('edit/', EditAuthor.as_view(), name='edit-author' ),
        path('delete/', DeleteAuthor.as_view(), name='delete-author' ),
    ]))
]