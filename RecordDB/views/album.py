from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from datetime import date, datetime
from RecordDB.forms import AlbumForm
from RecordDB.models import Artist
from RecordDB.models import Album
from RecordDB.models import Genre
from RecordDB.models import Track
from RecordDB.code import FileIO

def add_album(request, id):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['albumname']
            year = form.cleaned_data['year']

            # foreign keys
            g_id = request.POST['genres']
            genre = Genre.objects.filter(id=g_id)[0]
            artist = Artist.objects.filter(id=id)[0]

            f = request.FILES['cover']
            print(f)
            io = FileIO()
            saved_file = io.save_file(f)

            a = Album()
            a.album_name = name
            a.artist = artist
            a.genre = genre
            a.year = year
            a.cover_art = saved_file
            a.date_added = datetime.now()
            a.save()

            return redirect('/RecordDB/artist/' + str(id))
    else:
        form = AlbumForm()
        return render(request, 'RecordDB/album_form.html', {'form': form})

def album(request, id, artist_id):
    tracklist = Track.objects.filter(album_id=id)
    albumlist = Album.objects.filter(id=id)
    artistlist = Artist.objects.filter(id=artist_id)
    template = loader.get_template('RecordDB/album.html')
    context = {
        'track_list': tracklist,
        'album_list': albumlist,
        'artist_list': artistlist,
    }
    return HttpResponse(template.render(context, request))