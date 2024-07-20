import speech_recognition as sr
import webbrowser
import time
from time import ctime
import playsound
import random
import os
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if(ask):
            TalkMaster_speak(ask)
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening....")
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            TalkMaster_speak("Sorry could not recognize your voice\n")
        except sr.RequestError:
            TalkMaster_speak("Sorry. My speech service is down")
        return voice_data

def TalkMaster_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio- ' + str(r)+ '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        TalkMaster_speak('My name is chotu')
    if 'time' in voice_data:
        TalkMaster_speak(ctime())
    if 'search' in voice_data:
        search = record_audio("What do you want to search for? ")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        TalkMaster_speak("Here is what I found for " + search)
    if 'location' in voice_data:
        location = record_audio("What is the location? ")
        url = 'https://google.nl/maps/place/ ' + location + '/&amp'
        webbrowser.get().open(url)
        TalkMaster_speak("Here is the location of " + location)
    if 'exit' in voice_data:
        TalkMaster_speak("BYE")
        exit(0)

time.sleep(1)
TalkMaster_speak("Hello! My name is Talk Master")
TalkMaster_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)