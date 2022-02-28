# -*- coding: utf-8 -*-
"""
Simple voice assistant in Python using google Text-To-Speech api
"""
import os
import playsound
import speech_recognition as sr
from gtts import gTTS
import datetime
import os.path
import subprocess

def speak(text):
    tts = gTTS(text = text, lang = "es-us")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("voice.mp3")
    

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception" + str(e))

    return said.lower()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
        
    subprocess.Popen(["notepad.exe", file_name])
    

if __name__ == "__main__":
    
    wake_word = "infinium"
    
    while True:
        print("Escuchando")
        text_wake = get_audio()
        
        while text_wake.count(wake_word) > 0:
            
            
            text = get_audio()
            
            understand = 0
            
                # Notepad
            note_key_words = ["anotame esto", "toma nota", "escibime esto"]
            for key in note_key_words:
                if key in text:
                    note_text = get_audio()
                    note(note_text)
                    understand = 1
                    break
                    
                # Bienvenida    
            if "hola" in text:
                understand=1
                speak("Hola, ¿como estas?")
                break
                
                # Nombre
            if "como es tu nombre" in text:
                understand=1
                speak("Mi nombre es Infiniem")
                break
                
            if "hermosa" in text:
                understand=1
                speak("Carolina")
                break
                
            if "doctor" in text:
                understand=1
                speak("Otra vez estoy tomando falopa aaaaaaaa me encanta maldita falopa")
                break
                
            if understand==0:
            else:
                break
        
            