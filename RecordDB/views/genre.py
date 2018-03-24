from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from RecordDB.forms import GenreForm
from RecordDB.models import Genre

def genres(request):
    genre_list = Genre.objects.order_by('genre_name')
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