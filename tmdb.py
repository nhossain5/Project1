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

    return {
        'titles': list(get_title(k)),
    }