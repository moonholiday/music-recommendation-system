
# Music Recommendation System

A fully functional web-based music recommendation system that spits out recommendation based on the user input.



## Acknowledgements

 - [Playlist2vec: Spotify Million Playlist Dataset](https://zenodo.org/record/5002584)
 - [K Means](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html)



## API Reference

#### Get access token from spotify

```https
  GET accounts.spotify.com/api/token
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get resources

```https
  GET api.spotify.com/{version}/{resource_type}/{lookup_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


#### Get resources

```https
  GET api.spotify.com/v1/search
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `query`      | `string` | **Required**. name of item to fetch |

## Authors

- [@moonholiday](https://www.github.com/Moonholiday)


## Demo

![](https://github.com/Moonholiday/music-recommendation-system/blob/main/demo.gif)


## Installation

Install the project with pip

```bash
python -m venv env
pip install -r requirements.txt
python manage.py runserver
python manage.py tailwind start
```
    
