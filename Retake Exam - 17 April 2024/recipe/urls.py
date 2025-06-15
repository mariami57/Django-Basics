from django.urls import path, include

from recipe.views import RecipeCatalogue, CreateRecipe, DetailsRecipe, EditRecipe, DeleteRecipe

urlpatterns = [
    path('recipe/', include([
        path('catalogue/', RecipeCatalogue.as_view(), name='recipe-catalogue'),
        path('create/', CreateRecipe.as_view(), name='recipe-create'),
        path('<int:pk>/', include([
            path('details/', DetailsRecipe.as_view(), name='recipe-details'),
            path('edit/', EditRecipe.as_view(), name='recipe-edit'),
            path('delete/', DeleteRecipe.as_view(), name='recipe-delete'),
        ])),
    ]))
]