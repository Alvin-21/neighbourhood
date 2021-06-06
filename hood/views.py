from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
from .forms import *

# Create your views here.

def index(request):
    hood = Neighbourhood.objects.all()
    return render(request, 'index.html', {"hood": hood})

def hood(request, hood_id):
    single_hood = Neighbourhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood_id=hood)
    posts = Post.objects.filter(hood=hood)
    return render(request, 'hood.html', {"hood": single_hood, "business": business, "posts": posts})

def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile.html', {"profile": profile})

def create_hood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)

        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourhoodForm()

    return render(request, 'new_neighbourhood.html', {'form': form})

def create_business(request, hood_id):
    neighbourhood = Neighbourhood.objects.get(id=hood_id)

    if request.method == 'POST':
        form = BusinessForm(request.POST)

        if form.is_valid():
            business = form.save(commit=False)
            business.neighbourhood_id = neighbourhood
            business.user = request.user.profile
            business.save()
            return redirect('hood', neighbourhood.id)
    else:
        form = BusinessForm()

    return render(request, 'new_business.html', {"form": form})