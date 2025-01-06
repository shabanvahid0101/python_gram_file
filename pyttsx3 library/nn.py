import pyttsx3 as tts
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
import json
import time
import random
import pyjokes
import pywhatkit as kit
from googlesearch import search
from bs4 import BeautifulSoup
import urllib.request
import re
import sys
import pytz
import pyautogui
import pyperclip
from googletrans import Translator
from datetime import date
from datetime import datetime
from pytube import YouTube
from pytube import Playlist
from pytube import exceptions
from pytube import extract
from pytube import request
#from pytube import caption
from pytube import streams

engine = tts.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(' ', ' ')
    server.sendmail(' ', to, content)
    server.close()

def weather():
    speak("What is the name of the city?")
    city = takeCommand()
    api_key = " "
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        speak(" Temperature in kelvin unit is " + str(current_temperature) + "\n atmospheric pressure in hPa unit is " + str(current_pressure) + "\n humidity in percentage is " + str(current_humidiy) + "\n description  " + str(weather_description))
        
    else:
        speak("City Not Found")

def news():
    speak("lets check the news")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey= "
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        time.sleep(1)
        speak("Moving on to the next news..")
    speak("That's all for now")
    speak("Have a nice day")
    speak("Bye")
    exit()
    # Main Function
def main():
        while True:
            speak("Welcome to the virtual assistant")
            speak("How can I help you?")
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak("Searching wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                speak("Opening youtube")
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                speak("Opening google")
                webbrowser.open("google.com")
            elif 'play music' in query:
                speak("Playing music")
                music_dir = 'D:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'the time' in query:
                strTime = datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
            elif 'open code' in query:
                speak("Opening code")
                codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'email to' in query:
                speak("What should I say to email")
                content = takeCommand()
                to = " "
                sendEmail(to, content)
                speak("Email has been sent")
            elif 'weather' in query:
                speak("Checking weather")
                weather()
            elif 'news' in query:
                speak("Getting latest news")
                news()
            elif 'joke' in query:
                speak("Here's a joke for you")
                speak(pyjokes.get_joke())
            elif 'translate' in query:
                speak("What should I translate")
                text = takeCommand()
                translator = Translator()
                translated = translator.translate(text, dest='hi')
                speak(translated.text)
            elif 'search' in query:
                speak("Searching...")
                query = query.replace("search", "")
                for j in search(query, num=1, stop=1, pause=2):
                    webbrowser.open(j)
            elif 'download' in query:
                speak("What do you want to download?")
                download = takeCommand()
                kit.playonyt(download)
            elif 'location' in query:
                speak("What is the location?")
                location = takeCommand()
                webbrowser.open("https://www.google.com/maps/place/" + location)
            elif 'screenshot' in query:
                speak("Taking screenshot")
                screenshot = pyautogui.screenshot()
                screenshot.save("C:\\Users\\Admin\\Pictures\\screenshot.png")
                speak("Screenshot has been saved")
            elif 'copy' in query:
                speak("What do you want to copy?")
                copy = takeCommand()
                pyperclip.copy(copy)
                speak("Text has been copied")
            elif 'paste' in query:
                speak("Pasting text")
                speak(pyperclip.paste())
            elif 'exit' in query:
                speak("Exiting")
                speak("Have a nice day")
                speak("Bye")
                exit()
            else:
                speak("I am sorry, I cannot do that")
if __name__ == "__main__":
    main()
            

            