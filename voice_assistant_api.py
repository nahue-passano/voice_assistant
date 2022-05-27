import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from dotenv import load_dotenv
from pydantic import BaseModel
from speech_to_text import speech_to_text_wav2vec2 as stt_w2v2
import sounddevice as sd

    # Load weather api key
load_dotenv('api_keys.env')
api_key = os.getenv("OPENWEATHERMAP_KEY")

    # Load model of speech to text
model, processor = stt_w2v2.load_model()

    # Deploying FastAPI
app = FastAPI()

class Audio(BaseModel):
    audio_path: str

@app.get('/get-response-from-audio/')
async def get_response_from_audio(audio_path: Audio):
    
    audio_array = stt_w2v2.audio_to_array(audio_path.audio_path)

    predicted_sentence = stt_w2v2.inference_model(model, processor, audio_array)
    
    output = jsonable_encoder({'Prediction':predicted_sentence})
    """
    ### load audio
    # print(audio_path)
    ### STT
    ### NLP
    ### Information query
    # print(audio_path{'audio_path'})
    # # direccion web desde donde solicitaremos la informacion
    # try:
    #     base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #     #     city_name = "Ituzaingo"
    #     # esta es la URL completa con la informacion concatenada para realizar la petición correcta
    #     complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"	
    #     response = requests.get(complete_url)
    #     # Obtenemos la respuesta en formato JSON
    #     info = response.json()["main"]
    # except:
    #     info = 'que decis flaco'
    """
    return JSONResponse(output)

if __name__ == '__main__':
    import os
    os.system('uvicorn voice_assistant_api:app --reload')

    # url = 'http://127.0.0.1:8000'
    # endpoint = '/get-response-from-audio'
    # data = json.dumps({'audio_path': 'audio.wav'})
    # response = requests.post(url+endpoint, data=data)
    
