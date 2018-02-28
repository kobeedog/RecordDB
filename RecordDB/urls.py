from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genres', views.genres, name='genres'),
    path('add_genre', views.add_genre, name="add_genre"),
    path('add_artist', views.add_artist, name='add_artist'),
    path('artists', views.artists, name='artists'),
    path('artist/<int:id>/', views.artist, name="artist"),
    path('add_album/<int:id>/', views.add_album, name="add_album"),
    path('album/<int:id>/<int:artist_id>', views.album, name="album"),
    path('add_track/<int:id>/', views.add_track, name="add_track"),
    path('track/<int:id>/<int:album_id>', views.track, name="track"),
]