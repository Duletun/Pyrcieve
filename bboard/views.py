from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Bb
# просмотр модели
def index(request):
    bbs = Bb.objects.all()
    return render(request, 'index.html', {'bbs': bbs})