from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *

# Create your views here.

def index(request):
    return redirect(request, 'index.html')