import requests
import random
from random import randrange
from stop_words import get_stop_words

custom_stop_words = ['music', 'performance', 'people', 'musician', 'singer', 'dancer', 'band', 'many', 'no person']
for word in get_stop_words('en'): 
    custom_stop_words.append(word)

def get_playlist(keywords):
    """ Given a set of keywords, get_playlists returns Spotify playlists associated with those keywords """
    keywords = [keyword for keyword in keywords if keyword not in custom_stop_words]
    print(keywords)
    accessToken = get_access_token()
    payload = {'Authorization': 'Bearer ' + accessToken}
    final_playlist = {}
    for keyword in keywords:
        url = "https://api.spotify.com/v1/search?q=%22{0}%22&type=playlist".format(keyword)
        r = requests.get(url, data=payload)
        playlists = r.json()['playlists']['items']
        for playlist in playlists[0:2]:
            url = ""
            try:
                url = playlist['images'][1]['url']
            except IndexError:
                url = playlist['images'][0]['url']
            final_playlist[playlist['name']] = ("https://embed.spotify.com/?uri=" + playlist['uri'], url)
    return final_playlist

def get_access_token():
    """ Gets the access token to make requests """
    client_id = "3d10bf994f3e49f7ba82b6a837051e0d"
    client_secret = "2874f63f936d48eea5eff44682256998"
    grant_type = 'client_credentials'
    body_params = {'grant_type' : grant_type}
    url='https://accounts.spotify.com/api/token'
    response=requests.post(url, data=body_params, auth = (client_id, client_secret))
    return response.json()['access_token']
