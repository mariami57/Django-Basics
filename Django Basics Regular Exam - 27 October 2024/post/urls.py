from django.urls import path, include

from post.views import PostCreate, PostDetail, PostEdit, PostDelete

urlpatterns = [

    path('posts/', include([
        path('create/', PostCreate.as_view(), name='create-post'),
        path('<int:pk>/', include([
            path('details/', PostDetail.as_view(), name='details-post'),
            path('edit/', PostEdit.as_view(), name='edit-post'),
            path('delete/', PostDelete.as_view(), name='delete-post'),
        ]))
    ]))

]