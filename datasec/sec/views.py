from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse(content="Thanks, youb are connected")
