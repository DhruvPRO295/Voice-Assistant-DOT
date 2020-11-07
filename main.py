
# Importing modules
import pyttsx3
import speech_recognition as sr
import sys
import datetime
import time
import pathlib
import os
import os.path
from os import path
from selenium import webdriver
import random

# Variables for SPEAK function
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# SPEAK function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function for taking in user's voice input


def takeCommand():
    # Takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)

        # speak("I'm sorry I didn't get you..")
        print('Say that again please.')
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
