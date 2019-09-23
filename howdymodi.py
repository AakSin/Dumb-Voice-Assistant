import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')       #saari voices ki ek list aati hai
for i in voices:
    print(i.id)
engine.setProperty('voice', voices[1].id)   #voice female karta hai ye

engine.say("howdy modi")

engine.runAndWait()
