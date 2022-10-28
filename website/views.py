from django.http import HttpResponse
from datetime import datetime

def welcome(request):
  return HttpResponse('Welome to Meeting planner')
# Create your views here.

def date(request):
  return HttpResponse('This page was served at '+ str(datetime.now()))