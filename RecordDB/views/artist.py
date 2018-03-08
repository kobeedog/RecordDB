from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from datetime import date, datetime
from RecordDB.forms import ArtistForm
from RecordDB.models import Artist
from RecordDB.models import Album

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