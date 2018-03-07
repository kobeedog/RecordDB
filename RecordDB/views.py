from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from datetime import date, datetime
from .models import Genre
from .models import Artist
from .models import Album
from .models import Track
from .models import Configuration
from .forms import GenreForm
from .forms import ArtistForm
from .forms import AlbumForm
from .forms import TrackForm
from RecordDB.code import FileIO

def index(request):
    config_list = Configuration.objects.order_by('-parameter')
    template = loader.get_template('RecordDB/index.html')
    context = {
        'config_list': config_list,
    }
    return HttpResponse(template.render(context, request))

def genres(request):
    genre_list = Genre.objects.order_by('-id')
    template = loader.get_template('RecordDB/genres.html')
    context = {
        'genre_list': genre_list,
    }
    return HttpResponse(template.render(context, request))

def add_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['genrename']
            g = Genre(genre_name=name)
            g.save()
            genre_list = Genre.objects.order_by('-id')
            template = loader.get_template('RecordDB/genres.html')
            context = {
                'genre_list': genre_list,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = GenreForm()
        return render(request, 'RecordDB/genre.html', {'form': form})

def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['artistname']

            results = Artist.objects.filter(artist_name__iexact=name)
            if len(results) == 0:
                a = Artist(artist_name=name, date_added=datetime.now())
                a.save()

            artist_list = Artist.objects.order_by('-artist_name')
            template = loader.get_template('RecordDB/artists.html')
            context = {
                'artist_list': artist_list,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = ArtistForm()
        return render(request, 'RecordDB/artist_form.html', {'form': form})

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

def artists(request):
    artist_list = Artist.objects.order_by('-artist_name')
    template = loader.get_template('RecordDB/artists.html')
    context = {
        'artist_list': artist_list,
    }
    return HttpResponse(template.render(context, request))

def artist(request, id):
    #albumlist = Album.objects.select_related().filter(artist_id=id)
    artistlist = Artist.objects.filter(id=id)
    albumlist = Album.objects.filter(artist_id=id)
    template = loader.get_template('RecordDB/artist.html')
    context = {
        'artist_list': artistlist,
        'album_list': albumlist,
    }
    return HttpResponse(template.render(context, request))

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

def add_track(request, id):
    if request.method == "POST":
        form = TrackForm(request.POST)
        if form.is_valid():

            tracks = []
            t1 = form.cleaned_data['track1']
            t2 = form.cleaned_data['track2']
            t3 = form.cleaned_data['track3']
            t4 = form.cleaned_data['track4']
            t5 = form.cleaned_data['track5']
            t6 = form.cleaned_data['track6']
            t7 = form.cleaned_data['track7']
            t8 = form.cleaned_data['track8']
            t9 = form.cleaned_data['track9']
            t10 = form.cleaned_data['track10']
            t11 = form.cleaned_data['track11']
            t12 = form.cleaned_data['track12']

            tracks.append(t1)
            tracks.append(t2)
            tracks.append(t3)
            tracks.append(t4)
            tracks.append(t5)
            tracks.append(t6)
            tracks.append(t7)
            tracks.append(t8)
            tracks.append(t9)
            tracks.append(t10)
            tracks.append(t11)
            tracks.append(t12)

            for track in tracks:
                if len(track) > 0:
                    t = Track()
                    t.track_name = track
                    t.album = Album.objects.filter(id=id)[0]
                    t.save()

            tracks.clear()

            track_list = Track.objects.filter(album_id=id)
            album_list = Album.objects.filter(id=id)
            artist_id = album_list[0].artist.id

            template = loader.get_template('RecordDB/album.html')
            context = {
                'album_list': album_list,
                'track_list': track_list,
            }
            #return HttpResponse(template.render(context, request))
            return redirect('/RecordDB/album/' + str(id) + "/" + str(artist_id))
    else:
        form = TrackForm()
        return render(request, 'RecordDB/track_form.html', {'form': form})

def track(request, id, album_id):
    albumlist = Album.objects.filter(id=album_id)
    tracklist = Track.objects.filter(id=id)
    template = loader.get_template('RecordDB/track.html')
    context = {
        'track_list': tracklist,
        'album_list': albumlist,
    }
    return HttpResponse(template.render(context, request))