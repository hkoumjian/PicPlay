from clarifai.client import ClarifaiApi
from flask import Flask,abort,render_template,request,redirect,url_for
from werkzeug import secure_filename
import os
from spotify_playlist import *

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_keywords_for_image(img_url):
    """ Gets the keyword associated with the image through the Clarifai API """
    clarifai_api = ClarifaiApi() # assumes environment variables are set.
    result = clarifai_api.tag_images(open(img_url, "rb"))
    return result['results'][0]['result']['tag']['classes']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/list_playlists')
def show_playlists():
    keywords = get_keywords_for_image("clarifai_test_images/sea-dawn.jpg")
    playlists = get_playlist(keywords)
    return render_template("list_playlist.html", playlists=playlists)

if __name__ == '__main__':
    app.run(debug = True)
