from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from RecordDB.models import Configuration

def index(request):
    config_list = Configuration.objects.order_by('-parameter')
    template = loader.get_template('RecordDB/index.html')
    context = {
        'config_list': config_list,
    }
    return HttpResponse(template.render(context, request))