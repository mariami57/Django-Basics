from django.urls import path

from common.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]