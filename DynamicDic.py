import json
import os
from gtts import gTTS
import pyaudio
import playsound as ps
import speech_recognition as sr
from difflib import get_close_matches
#from unidecode import unidecodef
#from safeprint import print
data = json.loads(open("data.json").read())
w = input("Give Input ")
w = w.lower()

li = get_close_matches(w,data.keys(),6)

def speaker(words):
    intro_text = 'Does it mean'
    obj_first = gTTS(text=intro_text,lang='en')
    obj_first.save('asking.mp3')
    ps.playsound('asking.mp3')
    os.remove('asking.mp3')
    for i in words:
        obj_trial = gTTS(text=i,lang='en')
        obj_trial.save('Enquire.mp3')
        ps.playsound('Enquire.mp3')
        r = sr.Recognizer()
        with sr.Microphone as source:
