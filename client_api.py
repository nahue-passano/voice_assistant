import json
import requests

url = 'http://127.0.0.1:8000'
endpoint = '/get-response-from-audio/'
path = 'speech_to_text/test_voice.wav'

data_sent = json.dumps({'audio_path': path})

response = requests.get(url+endpoint, data = data_sent)
print(response.json())