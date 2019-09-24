############################################### setup etc. for voice
import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
engine = pyttsx3.init()

voices = engine.getProperty('voices')       #saari voices ki ek list aati hai

engine.setProperty("voice",voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate

############################################# datetime ka setup
day =  datetime. datetime.today().strftime('%A')
hour=str(datetime.datetime.now().hour)
minute=str(datetime.datetime.now().minute)



user=input("Enter your name ")


def speak(inp):
    engine.say(inp)
    engine.runAndWait() #blocks pyttsx waale functions till previous functions are complete

def intro():
    speak("Hi " +user+ "I am Kanye Best")
    
    speak("its " +hour+" "+minute+" right now and its a "+ day )
   
if __name__ == "__main__":
    intro()
 

