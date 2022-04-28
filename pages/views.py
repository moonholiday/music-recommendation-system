import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.http import HttpResponseRedirect
from .models import *
from .spotify_client import *
import json
import pickle
from slugify import slugify
import re
from pages.model1 import *
from .forms import AudioForm
from django.contrib.auth.decorators import login_required
from operator import is_not
from functools import partial

client_id="b4dad3bdf5144e6f8f408ec2f6f278a3"
client_secret="a1e9ff23036a4444abcf6067fd63c2ca"

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class FaqPageView(TemplateView):
    template_name = 'faq.html'

def GenrePageView(request):
    sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    genres = sp.categories(country='US', locale=None, limit=10, offset=0)
    # print(genres)
    # print(genre1)
    genre_list = genres['categories']['items']

    # print(genre_list)

    context = {'genre_list': genre_list}
    return render(request, 'genre.html', context = context)
    # test = sp.audio_features('68Dni7IE4VyPkTOH9mRWHr')
    # test1 = test
    # print(test1)

def genre_playlist(request):
    x = request.GET.get('x')
    li = ''
    if x is not None:
        li += list(x)



    # r = slugify(x)
    # f = re.sub('\-', '', r)
    # print(f)
    sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    playlist = sp.category_playlists(category_id='rock')
    pl_list = playlist['playlists']['items']
    context = {'pl_list': pl_list}
    # print(playlist)
    return render(request, 'genre_playlist.html', context=context)





def discover(request):
    query = request.POST.get('q')
    # if request.method=='POST':
    #     sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    #     result = sp.search(q=query, limit=20)
    #     print(result)
    #     new = []

    #     for idx, track in enumerate(result['tracks']['items']):
    #         new += (idx, track['name'], track['external_urls'])
    #
    #     return render(request, 'discover.html', {'result': new})
    # else:


    if request.method=='POST':
        spotify = SpotifyAPI(client_id, client_secret)
        recommendations = recommend_songs([{'name': query}])

        res_list = recommendations
        print(res_list)
    #
        return render(request, 'discover.html', {'res_list': res_list})
    else:
        return render(request, 'discover.html')



# category list view
def free_music(request):
    # display all genres
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'free_music.html', context=context)

# song list view of each category
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

@login_required
def add_music(request):

    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()
    else:
        form = AudioForm()
    return render(request, 'add_music.html', {'form':form})
