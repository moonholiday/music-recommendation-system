#!/usr/bin/env python
from collections import defaultdict
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from scipy.spatial.distance import cdist


data = pd.read_csv("data.csv")
genre_data = pd.read_csv('data_by_genres.csv')
data.head()

cluster_pipeline = Pipeline(
    [('scaler', StandardScaler()), ('kmeans', KMeans(n_clusters=10, n_init=10))])
X = genre_data.select_dtypes(np.number)
cluster_pipeline.fit(X)
genre_data['cluster'] = cluster_pipeline.predict(X)
tsne_pipeline = Pipeline(
    [('scaler', StandardScaler()), ('tsne', TSNE(n_components=2, verbose=1))])
genre_embedding = tsne_pipeline.fit_transform(X)

song_cluster_pipeline = Pipeline([('scaler', StandardScaler()),
                                  ('kmeans', KMeans(n_clusters=20,
                                   verbose=False))
                                  ], verbose=False)

X = data.select_dtypes(np.number)
number_cols = list(X.columns)
song_cluster_pipeline.fit(X)
song_cluster_labels = song_cluster_pipeline.predict(X)
data['cluster_label'] = song_cluster_labels
pca_pipeline = Pipeline([('scaler', StandardScaler()),
                        ('PCA', PCA(n_components=2))])
song_embedding = pca_pipeline.fit_transform(X)
client_id = "b4dad3bdf5144e6f8f408ec2f6f278a3"
client_secret = "a1e9ff23036a4444abcf6067fd63c2ca"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret))


def find_song(name):
    song_data = defaultdict()
    results = sp.search(q=name, limit=1)
    if results['tracks']['items'] == []:
        return None

    results = results['tracks']['items'][0]
    track_id = results['id']
    audio_features = sp.audio_features(track_id)[0]

    song_data['name'] = [name]
    song_data['explicit'] = [int(results['explicit'])]
    song_data['duration_ms'] = [results['duration_ms']]
    song_data['popularity'] = [results['popularity']]

    for key, value in audio_features.items():
        song_data[key] = value

    return pd.DataFrame(song_data)


number_cols = ['valence', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
               'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']


class Rec:

    def get_song_data(song, spotify_data):

        try:
            song_data = spotify_data[(
                spotify_data['name'] == song['name'])].iloc[0]
            return song_data

        except IndexError:
            return find_song(song['name'])

    def get_mean_vector(song_list, spotify_data):

        song_vectors = []

        for song in song_list:
            song_data = Rec.get_song_data(song, spotify_data)
            if song_data is None:
                print('Warning: {} does not exist in Spotify or in database'.format(
                    song['name']))
                continue
            song_vector = song_data[number_cols].values
            song_vectors.append(song_vector)

        song_matrix = np.array(list(song_vectors))
        return np.mean(song_matrix, axis=0)

    def flatten_dict_list(dict_list):

        flattened_dict = defaultdict()
        for key in dict_list[0].keys():
            flattened_dict[key] = []

        for dictionary in dict_list:
            for key, value in dictionary.items():
                flattened_dict[key].append(value)

        return flattened_dict

    def recommend_songs(song_list, spotify_data, n_songs=10):

        metadata_cols = ['name', 'id', 'artists']
        song_dict = Rec.flatten_dict_list(song_list)

        song_center = Rec.get_mean_vector(song_list, spotify_data)
        scaler = song_cluster_pipeline.steps[0][1]
        scaled_data = scaler.transform(spotify_data[number_cols])
        scaled_song_center = scaler.transform(song_center.reshape(1, -1))
        distances = cdist(scaled_song_center, scaled_data, 'cosine')
        index = list(np.argsort(distances)[:, :n_songs][0])

        rec_songs = spotify_data.iloc[index]
        rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]
        return rec_songs[metadata_cols].to_dict(orient='records')
