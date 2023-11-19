'''note : who are having these modules in their system then only
this application will be working or else you can download these modules'''
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
voice = engine.getProperty('voices')

def command():
    r = sr.Recognizer()
    print("listening...")
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Processing...")
        audio_text = r.recognize_google(audio,language='en-in')
        print(audio_text)

    except Exception as e:
        print("say again")
        audio_text = None

    return audio_text

if __name__ == "__main__":
    c=1
    while c!=2:
        query = command().lower()

        if 'open youtube' in query:
            url='youtube.com'
            engine.say("Opening youtube ")
            webbrowser.open(url)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            engine.say(f"sir,the time is {strTime}")
            engine.runAndWait()

        elif 'thanks' in query:
            c = int(c) + 1
            engine.say("Your welcome sir")
            engine.runAndWait()
