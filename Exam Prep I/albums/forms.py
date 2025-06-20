from django import forms

from albums.choices import GenreChoices
from albums.mixins import ReadOnlyMixin
from albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']
        widgets = {"album_name": forms.TextInput(attrs={"placeholder": "Album Name"}),
                    "artist": forms.TextInput(attrs={"placeholder": "Artist"}),
                    "genre":forms.Select(choices=GenreChoices.choices, attrs={"placeholder": "Genre:"}),
                    "description": forms.Textarea(attrs={"placeholder": "Description"}),
                   "image_url": forms.URLInput(attrs={"placeholder": "Image URL"}),
                   "price": forms.NumberInput(attrs={"placeholder": "Price"}),
                   }
        labels = {
            "album_name": "Album Name:",
            "artist": "Artist:",
            "genre": "Genre:",
            "description": "Description:",
            "image_url": "Image URL:",
            "price": "Price:",
        }

class CreateAlbumForm(AlbumBaseForm):
    ...

class EditAlbumForm(AlbumBaseForm):
    ...

class DeleteAlbumForm(ReadOnlyMixin, AlbumBaseForm):
    ...