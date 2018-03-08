from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from RecordDB.forms import TrackForm
from RecordDB.forms import AlbumForm
from RecordDB.models import Artist
from RecordDB.models import Album
from RecordDB.models import Genre
from RecordDB.models import Track

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
