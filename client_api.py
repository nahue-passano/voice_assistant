import json
import requests

url = 'http://127.0.0.1:8000'
endpoint = '/get-response-from-audio'
path = 'speech_to_text/test_voice.wav'
response = requests.get(url+endpoint+'?audio_path='+path)
print(response.json)