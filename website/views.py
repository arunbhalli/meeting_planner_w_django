from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from meetings.models import Meeting


def welcome(request):
    return render(request, 'website/welcome.html', 
                  {"meetings": Meeting.objects.all()})
# Create your views here.


def date(request):
    return HttpResponse('This page was served at ' + str(datetime.now()))


def about(request):
    return HttpResponse('I am Arun and i am a good planner ')
