from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView

from author.models import Profile
from recipe.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from recipe.models import Recipe


# Create your views here.
class RecipeCatalogue(ListView):
    model = Recipe
    template_name = "recipe/catalogue.html"


class CreateRecipe(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = "recipe/create-recipe.html"
    success_url = reverse_lazy("recipe-catalogue")

    def form_valid(self, form):
        profile = Profile.objects.first()  # or use some specific Profile
        form.instance.author = profile
        return super().form_valid(form)

class EditRecipe(UpdateView):
    model = Recipe
    form_class = RecipeEditForm
    template_name = "recipe/edit-recipe.html"
    success_url = reverse_lazy("recipe-catalogue")

class DeleteRecipe(DeleteView, FormView):
    model = Recipe
    form_class = RecipeDeleteForm
    template_name = "recipe/delete-recipe.html"
    success_url = reverse_lazy("recipe-catalogue")

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        recipe = self.model.objects.get(pk=pk)
        return recipe.__dict__

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

class DetailsRecipe(DetailView):
    model = Recipe
    template_name = "recipe/details-recipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object
        context['ingredients_list'] = recipe.ingredients.split(', ')
        return context
