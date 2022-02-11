import os
import requests
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
        params=params,
    )
    data = response.json()

    def get_title(i):
        titles = []
        for j in range(i):
            titles.append(data["results"][j]["title"])
        return titles
        #return data["results"]

    def get_poster_path(i):
        poster_paths = []
        for j in range(i):
            poster_paths.append(data["results"][j]["poster_path"])
        return poster_paths

    def get_overview(i):
        overviews = []
        for j in range(i):
            overviews.append(data["results"][j]["overview"])
        return overviews

    return {
        'titles': list(get_title(k)),
        'poster_paths': list(get_poster_path(k)),
        'overviews': list(get_overview(k))
    }