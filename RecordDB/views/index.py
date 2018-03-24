from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from RecordDB.models import Configuration
from RecordDB.models import Artist
from RecordDB.models import Album
from RecordDB.models import Track

def index(request):
    config_list = Configuration.objects.order_by('-parameter')

    template = loader.get_template('RecordDB/index.html')
    artist_count = Artist.objects.count()
    album_count = Album.objects.count()
    track_count = Track.objects.count()

    print(str(artist_count))
    context = {
        'config_list': config_list,
        'artist_count': artist_count,
        'album_count': album_count,
        'track_count': track_count,
    }
    return HttpResponse(template.render(context, request))