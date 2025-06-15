from django.urls import path, include

from cars.views import CarCatalogueView, CarCreateView, CarDetailView, CarEditView, CarDeleteView

urlpatterns = [
    path('car/', include([
        path('catalogue/', CarCatalogueView.as_view(), name='car-catalogue'),
        path('create/', CarCreateView.as_view(), name='car-create'),
        path('<int:pk>/', include([
            path('details/', CarDetailView.as_view(), name='car-details'),
            path('edit/', CarEditView.as_view(), name='car-edit'),
            path('delete/', CarDeleteView.as_view(), name='car-delete'),
        ])),
    ]))
]