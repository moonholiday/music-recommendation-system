import pickle

with open('song_recommendation', 'rb') as f:
    model = pickle.load(f)
