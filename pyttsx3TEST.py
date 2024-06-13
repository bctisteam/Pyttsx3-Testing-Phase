''''import pyttsx3
engine = pyttsx3.init()
engine.say("Hi My name is andrew allen, and welcome to the barrett building here at humber college, we are goin to do alot interesting things")
engine.runAndWait()'''

import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate =  engine.getProperty('rate')
engine.setProperty('rate', rate-10)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Hi My name is andrew allen, and welcome to the barrett building here at humber college, we're goin to do alot of interesting things")