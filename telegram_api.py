import json
import requests

url = 'http://127.0.0.1:8000'
endpoint = '/get-response-from-audio'
path = 'audio.mp3'
response = requests.get(url+endpoint+'?audio_path='+path)
print(response.json)