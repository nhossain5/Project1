import os
from flask import Flask, render_template
from tmdb import get_movie_data

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=["POST", "GET"])
def hello_world():
    movie_data = get_movie_data(20)
    return render_template(
        "index.html",
        titles=movie_data['titles']
    )

app.run(
    host='0.0.0.0',
    port=int(os.getenv('PORT', 8080)),
    debug=True
)