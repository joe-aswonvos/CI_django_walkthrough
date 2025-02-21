from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(about_me):
    return HttpResponse('This is the about view')   # This is the response that will be sent to the client
