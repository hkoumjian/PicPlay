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

    clarifai_api = ClarifaiApi("_O7oVw0TVQ2SC7l3Bwkb_UJ95LAzE8amEMQp0VGr", "hAhcV7cMgFmXDq-91Bvbk-V5FEaL1dTfTxtVtRzz") # assumes environment variables are set.
    # result = clarifai_api.tag_images(open(img_url, "rb"))
    result = clarifai_api.tag_image_urls(img_url)
    return result['results'][0]['result']['tag']['classes']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/list_playlists', methods=['POST'])
def list_playlists():
	keywords = get_keywords_for_image(request.form['img_search'])
	playlists = get_playlist(keywords)
	return render_template("list_playlist.html", playlists=playlists)

if __name__ == '__main__':
    app.run(debug = True, threaded=True)
