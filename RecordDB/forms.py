from django import forms
from django.forms import TextInput

from .models import Genre

def load_genres():
    tuple_list = []
    list = Genre.objects.all().order_by('genre_name')
    for l in list:
        tuple_list.append((l.id, l.genre_name))
    return tuple_list

class GenreForm(forms.Form):
    genrename = forms.CharField(label="Genre Name", max_length=100)

class ArtistForm(forms.Form):
    artistname = forms.CharField(label="Artist Name", max_length=400)

class AlbumForm(forms.Form):
    albumname = forms.CharField(label="Album Name", max_length=400)
    genres = forms.ChoiceField(choices=load_genres(), required=True)
    year = forms.CharField(widget=TextInput(attrs={'type':'number'}))
    cover = forms.ImageField(label="Cover", required=False)

class TrackForm(forms.Form):
    track1 = forms.CharField(label="", max_length=400)
    track2 = forms.CharField(label="", max_length=400, required=False)
    track3 = forms.CharField(label="", max_length=400, required=False)
    track4 = forms.CharField(label="", max_length=400, required=False)
    track5 = forms.CharField(label="", max_length=400, required=False)
    track6 = forms.CharField(label="", max_length=400, required=False)
    track7 = forms.CharField(label="", max_length=400, required=False)
    track8 = forms.CharField(label="", max_length=400, required=False)
    track9 = forms.CharField(label="", max_length=400, required=False)
    track10 = forms.CharField(label="", max_length=400, required=False)
    track11 = forms.CharField(label="", max_length=400, required=False)
    track12 = forms.CharField(label="", max_length=400, required=False)