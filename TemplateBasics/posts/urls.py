from django.conf.urls.static import static
from django.contrib.sitemaps.views import index
from django.urls.conf import path

from forumApp import settings
from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-post/', views.add_post, name='add_post'),
    path('edit-post/<int:pk>/', views.edit_post, name='edit_post'),
    path('details-post/<int:pk>/', views.post_details, name='details_post'),
    path('delete-post/<int:pk>/', views.delete_post, name='delete_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)