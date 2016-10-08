import requests


def getPlaylist(keywords):
    authReq = requests.get('https://accounts.spotify.com/authorize', data = {
        'client_id':'0aa450070bda4ca2a963c9c550cad0bc',
        'response_type':'code',
        'redirect_uri':'index.html'
    })
    for key in keywords
        r = requests.post('https://api.spotify.com/v1/search', data = {
            'Authorization':auth,
            'q':key,
            'type':'playlist'
            })
