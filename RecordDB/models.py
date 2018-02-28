from django.db import models

class Artist(models.Model):
    id = models.IntegerField(primary_key=True)
    artist_name = models.CharField(max_length=455)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'artist'

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    genre_name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'genre'

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    album_name = models.CharField(max_length=455)
    cover_art = models.CharField(max_length=455)
    date_added = models.DateTimeField()
    year = models.IntegerField(primary_key=False)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'album'

class Track(models.Model):
    id = models.IntegerField(primary_key=True)
    track_name = models.CharField(max_length=500)

    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'track'


