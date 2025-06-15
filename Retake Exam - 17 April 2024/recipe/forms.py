from django import forms

from recipe.mixins import ReadOnlyMixin
from recipe.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)
        help_texts = {
            "ingredients":"Ingredients must be separated by a comma and space.",
            "cooking_time": "Provide the cooking time in minutes.",

        }
        error_messages = {
            "title":{
                "unique":"We already have a recipe with the same title!",
            }
        }

        labels = {
            "title": "Title:",
            "cuisine_type": "Cuisine Type:",
            "ingredients": "Ingredients:",
            "instructions": "Instructions:",
            "cooking_time": "Cooking Time:",
            "image_url":"Image URL"
        }


class RecipeCreateForm(RecipeBaseForm):
    class Meta(RecipeBaseForm.Meta):
        widgets = {
            "ingredients": forms.Textarea(attrs={"placeholder":"ingredient1, ingredient2, ...", "rows":6}),
            "instructions": forms.Textarea(attrs={"placeholder":"Enter detailed instructions here...", "rows":5}),
            "image_url": forms.TextInput(attrs={"placeholder":"Optional image URL here..."}),

        }
class RecipeEditForm(RecipeBaseForm):
    ...

class RecipeDeleteForm(ReadOnlyMixin, RecipeBaseForm):
    ...