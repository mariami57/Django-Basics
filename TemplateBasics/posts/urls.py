from django.contrib.sitemaps.views import index
from django.urls.conf import path

from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
]