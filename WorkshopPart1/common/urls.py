from django.urls import path, include

from common import views

urlpatterns = [
    path("", views.home_page_view, name="home"),


    path('<int:photo_id>/', include([
        path('like/', views.like_functionality, name="like"),
        path('share/', views.share, name="share"),
        path('comment/', views.add_comment, name="add_comment"),
    ]))
]