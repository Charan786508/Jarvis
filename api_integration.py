import requests

class APIIntegration:
    def __init__(self):
        pass

    def get_weather(self, city, api_key):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={{city}}&appid={{api_key}}'
        response = requests.get(url)
        return response.json()

    def get_wikipedia_summary(self, title):
        url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{{title}}'
        response = requests.get(url)
        return response.json()

    def get_music_playlist(self, service, api_key):
        # This is a placeholder function. You need to implement API calls for specific music services.
        if service == 'Spotify':
            url = f'https://api.spotify.com/v1/me/playlists'
            headers = {'Authorization': f'Bearer {{api_key}}'}
            response = requests.get(url, headers=headers)
            return response.json()
        elif service == 'Apple Music':
            url = f'https://api.music.apple.com/v1/me/playlists'
            headers = {'Authorization': f'Bearer {{api_key}}'}
            response = requests.get(url, headers=headers)
            return response.json()
        else:
            return {'error': 'Unsupported music service'}
