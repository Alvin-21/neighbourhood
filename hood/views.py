from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    hood = Neighbourhood.objects.all()
    return render(request, 'index.html', {"hoods": hood})

@login_required(login_url='/accounts/login/')
def hood(request, hood_id):
    single_hood = Neighbourhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood_id=single_hood)
    posts = Post.objects.filter(hood=single_hood)
    return render(request, 'hood.html', {"hood": single_hood, "businesses": business, "posts": posts})

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile.html', {"profile": profile})

@login_required(login_url='/accounts/login/')
def create_hood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)

        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user
            hood.save()
            return redirect('hood', hood.id)
    else:
        form = NeighbourhoodForm()

    return render(request, 'new_neighbourhood.html', {'form': form})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def create_post(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.profile = request.user.profile
            post.save()
        return redirect('hood', hood.id)
    else:
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})

@login_required(login_url='/accounts/login/')
def edit_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)

        if form.is_valid():
            edit_profile = form.save(commit=False)
            edit_profile.save()
        return redirect('profile', profile.id)
    else:
        form = EditProfileForm()
    return render(request, 'edit_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def join_hood(request, hood_id):
    hood = get_object_or_404(Neighbourhood, id=hood_id)
    request.user.profile.neighbourhood_id = hood
    request.user.profile.save()
    occupants = hood.occupants + 1
    hood.occupants = occupants
    hood.save()
    return HttpResponseRedirect(reverse('homepage'))

@login_required(login_url='/accounts/login/')
def leave_hood(request, hood_id):
    hood = get_object_or_404(Neighbourhood, id=hood_id)
    request.user.profile.neighbourhood_id = None
    request.user.profile.save()
    occupants = hood.occupants - 1
    hood.occupants = occupants
    hood.save()
    return HttpResponseRedirect(reverse('homepage'))