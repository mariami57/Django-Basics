from django import forms

from post.mixins import ReadOnlyMixin
from post.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude=("updated_at", "author")

        help_texts = {
            "image_url": "Share your funniest furry photo URL!",
        }

        error_messages = {
            "title": {
                "unique":"Oops! That title is already taken. How about something fresh and fun?",
            }
        }

        labels = {
            "title":"Title:",
            "image_url":"Post Image URL:",
            "content":"Content:",
        }

class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Put an attractive and unique title..."}),
            "content": forms.Textarea(attrs={"placeholder": "Share some interesting facts about your adorable pets..."}),
        }


class PostEditForm(PostBaseForm):
    ...

class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    ...

