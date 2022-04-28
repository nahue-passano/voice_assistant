from fastapi import FastAPI, Path, Request
from typing import Optional
import requests, json, os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv('weather_api_key.env')
api_key = os.getenv("OPENWEATHERMAP_KEY")

app = FastAPI()


@app.get('/')
def home():
    return {'Data': 'Test'}

@app.get('/get-response-from-audio')
def get_response_from_audio(audio_path: str):
    ### load audio
    # print(audio_path)
    ### STT
    ### NLP
    ### Information query
    print(audio_path)
    # direccion web desde donde solicitaremos la informacion
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        # ciudad (se lo mas especifico posible en el nombre)
        city_name = "Ituzaingo"
        # esta es la URL completa con la informacion concatenada para realizar la petición correcta
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"	
        # Ejecutamos la consulta
        response = requests.get(complete_url)
        # Obtenemos la respuesta en formato JSON
        info = response.json()["main"]
    except:
        info = 'que decis flaco'
    return {'Response': info, 'Audio path': audio_path}

if __name__ == '__main__':
    import os
    os.system('uvicorn voice_assistant_api:app --reload')

    # url = 'http://127.0.0.1:8000'
    # endpoint = '/get-response-from-audio'
    # data = json.dumps({'audio_path': 'audio.wav'})
    # response = requests.post(url+endpoint, data=data)
    
