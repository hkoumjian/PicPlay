import requests

def get_playlist(keywords):
    accessToken = "BQC0XYHgXg71_vBytbhPP5j8QVZq1QBKmY7w3oHjCXfr3GFdhGzvT8iv9taj9RnwwkWf9GoVmDqshUpYyQVnmWlZxoj91L4LxiYLs5UjSrkqqFClaJBnOJXt3zqvWis8VmDMv-fLcO9D2eElCubaS6zvADEKI7veK5Rc3mgWi-kItKa3RGVgGAMFMnuv4e3FdkwTczLd2SOqP4IeGksF5T7DvYMDxPDTrtGoD-3KANdSkjLxWulQ5E14BQ"
    payload = {'Authorization': 'Bearer ' + accessToken}
    final_playlist = {}
    for keyword in keywords:
        url = "https://api.spotify.com/v1/search?q=%22{0}%22&type=playlist".format(keyword)
        r = requests.get(url, params=payload)
        playlists = r.json()['playlists']['items']
        for playlist in playlists[0:2]:
            final_playlist[playlist['name']] = ("https://embed.spotify.com/?uri=" + playlist['uri'], playlist['images'][2]['url'])
    return final_playlist
