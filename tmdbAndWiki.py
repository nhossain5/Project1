import os
import requests
import random
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/trending/movie/day"
TMDB_KEY = os.getenv("TMDB_KEY")

def get_movie_data(k):
    params = {
    "api_key": TMDB_KEY
    }

    response = requests.get(
        BASE_URL,
        params=params
        )
    data = response.json()

    r = random.randint(0,19)

    id = data["results"][r]["id"]

    def get_id(i):
        ids = []
        for j in range(i):
            ids.append(data["results"][r]["id"])
        return ids

    def get_genre(i):
        GENRE_URL = "https://api.themoviedb.org/3/movie/" + str(id) + "?"
        genre_params = {
            "movie_id": get_id(i),
            "api_key": TMDB_KEY
            }
        genre_response = requests.get(
            GENRE_URL,
            params=genre_params
            )
        genre_data = genre_response.json()
        genres = []
        for j in range(i):
            genres.append(genre_data["genres"][0]["name"])
        return genres

    def get_title(i):
        titles = []
        for j in range(i):
            titles.append(data["results"][r]["title"])
        return titles
        #return data["results"]

    def get_poster_path(i):
        poster_paths = []
        for j in range(i):
            poster_paths.append(data["results"][r]["poster_path"])
        return poster_paths

    def get_tagline(i):
        TAGLINE_URL = "https://api.themoviedb.org/3/movie/" + str(id) + "?"
        tagline_params = {
            "movie_id": get_id(i),
            "api_key": TMDB_KEY
            }
        tagline_response = requests.get(
            TAGLINE_URL,
            params=tagline_params
            )
        tagline_data = tagline_response.json()
        taglines = []
        for j in range(i):
            taglines.append(tagline_data["tagline"])
        return taglines

    def get_wikilink(i):
        WIKI_URL = 'https://en.wikipedia.org/w/api.php'
        title = get_title(i)
        wikilink_params = {
            'action': 'query',
            'format': 'json',
            "list": "search",
            "srsearch": title[0] + " articletopic:films"
            }
        wikilink_response = requests.get(
            WIKI_URL,
            params=wikilink_params
            )
        wikilink_data = wikilink_response.json()
        wikilinks = []
        for j in range(i):
            wikilinks.append("https://en.wikipedia.org/?curid="+str(wikilink_data["query"]["search"][0]["pageid"]))
        return wikilinks

    return {
        'titles': list(get_title(k)),
        'poster_paths': list(get_poster_path(k)),
        'taglines': list(get_tagline(k)),
        'ids' : list(get_id(k)),
        'genres' : list(get_genre(k)),
        'wikilinks' : list(get_wikilink(k))
    }