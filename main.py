############################################### setup etc. for voice, SpeechRecognition
"""
before running this file make sure to go to command prompt 
open it in this directory
and then type "pip install -r requirements.txt"
it will automatically install all the dependencies
"""

import pyttsx3  #pip install pyttsx3
import pyaudio  #pip install pyaudio
import speech_recognition as sr #pip install speechRecognition
import datetime
import os
from selenium import webdriver #pip install selenium
from selenium.webdriver.common.keys import Keys #download chromedriver first and update your chrome to version 76
import time
import json

js=open("pw.json")
base=json.load(js)

engine = pyttsx3.init()

voices = engine.getProperty('voices')       #saari voices ki ek list aati hai

engine.setProperty("voice",voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 175)     # setting up new voice rate

############################################# datetime ka setup
day =  datetime. datetime.today().strftime('%A')
hour=str(datetime.datetime.now().hour)
minute=str(datetime.datetime.now().minute)

############################################ my functions


def speak(inp):
    engine.say(inp)
    engine.runAndWait() #blocks pyttsx waale functions till previous functions are complete

def intro():
    global user
    user=input("Enter your name ")
    speak(f"Hi {user} I am new gen bot")
    
    speak(f"its {hour} {minute} right now and its a {day}" )

def listenTo():
    #for taking microphone input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 900
        r.pause_threshold=0.5
        audio = r.listen(source)

    try:
        print("Understanding..")    
        query = r.recognize_google(audio, language='en-in') #en-in is english india and yaha pe we have used the google audio engine
        print("User said:"+ query)

    except : 
        print("Could you repeat that?")
        return "none" 
    return query

def search_google(query):
    query=query.replace("google ","")
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(query)
    search.send_keys(Keys.ENTER)
    try:
        res=browser.find_element_by_class_name("Z0LcW")
        speak(res.text)
    except:
        pass
    try:
        res=browser.find_element_by_class_name("e24Kjd")
        speak(res.text)
    except:
        pass
def play_youtube(query):
    query=query.replace("youtube ","")
    browser = webdriver.Chrome()
    browser.get(f"https://www.youtube.com/results?search_query={query}")
    for i in browser.find_elements_by_id("video-title"):
        if "ytd-promoted-video-renderer" in i.get_attribute("class"):
            print(i.get_attribute("class"))
            continue
        else:
            res=i
            break
    res.click()
def topReddit(query):
    query=query.replace("reddit ","")
    query=query.replace(" ","")
    browser = webdriver.Chrome()
    browser.get(f"https://www.reddit.com/r/{query}/top/?t=week")

##################################### Actual Program

if __name__ == "__main__":
    
    #intro()
    while True:    
        query=listenTo().lower()
        if "google"==query[:6]:
            search_google(query)
        if "youtube"==query[:7]:
            play_youtube(query)
        if "reddit"==query[:6]:
            topReddit(query)
        if query=="exit":   
            exit()
        os.system("pause")