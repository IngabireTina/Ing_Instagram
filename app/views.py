from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# Create your views here.

def home(request):
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    form = PostForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user.profileImg
        post.save()
        return redirect('home')
    context = {
        'posts': posts,
        'form': form,
        'users':users,
    }
    return render(request, 'home.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

        else: 
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def profile(request, username):
    images = request.user.profileImg.posts.all()
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profileImg)
        if prof_form.is_valid():
            prof_form.save()
            return redirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    context = {
        'prof_form': prof_form,
        'images': images,

    }
    return render(request, 'profile.html', context)

      
