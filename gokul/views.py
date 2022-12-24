from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def name(request):
    return HttpResponse('<marquee>it is the gokul</marquee>')
