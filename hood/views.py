from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *

# Create your views here.

def index(request):
    hood = Neighbourhood.objects.all()
    return render(request, 'index.html', {"hood": hood})

def hood(request, hood_id):
    single_hood = Neighbourhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood_id=hood)
    posts = Post.objects.filter(hood=hood)
    return render(request, 'hood.html', {"hood": single_hood, "business": business, "posts": posts})

