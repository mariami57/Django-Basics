from django.urls import path

from common.views import index, Dashboard

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

]