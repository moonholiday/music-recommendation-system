import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .spotify_client import *
import json
import pickle
from slugify import slugify
import re
from pages.model1 import *
from .forms import AudioForm
from django.contrib.auth.decorators import login_required

client_id = "b4dad3bdf5144e6f8f408ec2f6f278a3"
client_secret = "a1e9ff23036a4444abcf6067fd63c2ca"


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class FaqPageView(TemplateView):
    template_name = 'faq.html'


def GenrePageView(request):
    x = request.POST.get('x')
    # print(x)
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret))
    genres = sp.categories(locale=None, limit=10, offset=0)
    print(genres)
    # print(genre1)
    if x is None:
        genre_list = genres['categories']['items']

        # print(genre_list)
        # if request.GET.get('x') is not None:
        context = {'genre_list': genre_list}
        return render(request, 'genre.html', context=context)

    if x is not None:
        r = slugify(x)
        f = re.sub('-', '', r)
        playlist = sp.category_playlists(category_id=f)
        pl_list = playlist['playlists']['items']
        context = {'pl_list': pl_list}
        # print(pl_list)
        return render(request, 'genre.html', context=context)


def discover(request):
    query = request.POST.get('q')

    if request.method == 'POST':
        spotify = SpotifyAPI(client_id, client_secret)
        recommendations = recommend_songs([{'name': query}])

        res_list = recommendations
        # print(res_list)
    #
        return render(request, 'discover.html', {'res_list': res_list})
    else:
        return render(request, 'discover.html')


def free_music(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'free_music.html', context=context)


def single_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    songs = Song.objects.filter(category=category)
    song_list = list(Song.objects.all().values())

    context = {
        'category': category,
        'songs': songs,
        'song_list': song_list,
    }

    return render(request, 'single_category.html', context=context)


@login_required(login_url='login')
def add_music(request):

    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)

        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            name1 = form.cleaned_data['category']
            name2 = form.cleaned_data['song_img']
            name3 = form.cleaned_data['artist']
            name4 = form.cleaned_data['song_file']
            Song(user=usr, name=name, category=name1, song_img=name2,
                 artist=name3, song_file=name4).save()
    else:
        form = AudioForm()
    return render(request, 'add_music.html', {'form': form})


@login_required(login_url='login')
def update_music(request, pk):
    song = Song.objects.get(id=pk)
    form = AudioForm(instance=song)
    if request.method == 'POST':
        form = AudioForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'add_music.html', {'form': form})


@login_required(login_url='login')
def delete_music(request, pk):
    song = Song.objects.get(id=pk)
    song.delete()
    return redirect('dashboard')
