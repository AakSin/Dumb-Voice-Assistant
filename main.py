############################################### setup etc. for voice
import pyttsx3  #pip install pyttsx3
import pyaudio  #pip install pyaudio
import speech_recognition as sr #pip install speechRecognition
import datetime
import os

engine = pyttsx3.init()

voices = engine.getProperty('voices')       #saari voices ki ek list aati hai

engine.setProperty("voice",voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate

############################################# datetime ka setup
day =  datetime. datetime.today().strftime('%A')
hour=str(datetime.datetime.now().hour)
minute=str(datetime.datetime.now().minute)

############################################ my functions

user=input("Enter your name ")


def speak(inp):
    engine.say(inp)
    engine.runAndWait() #blocks pyttsx waale functions till previous functions are complete

def intro():
    speak("Hi " +user+ "I am Kanye Best")
    
    speak("its " +hour+" "+minute+" right now and its a "+ day )

def listenTo():
    #for taking microphone input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 700
        audio = r.listen(source)

    try:
        print("Understanding..")    
        query = r.recognize_google(audio, language='en-in') #en-in is english india and yaha pe we have used the google audio engine
        print("User said:"+ query)

    except : 
        print("Could you repeat that?")
        return "none"  
    return query
##################################### Actual Program

if __name__ == "__main__":
    intro()
    query=listenTo().lower()
    os.system("pause")