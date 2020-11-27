
# Importing modules
import nltk.corpus
import nltk
import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path
import os.path
import os
import pyttsx3
import speech_recognition as sr
import sys
import datetime
import time
import webbrowser
import pathlib
import json

# Variables for SPEAK function
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def RUN_CHROME_DRIVER():
    global DRIVER
    DRIVER = webdriver.Chrome(
        executable_path='C:\\Program Files (x86)\\Selenium\\chromedriver.exe')


def QUIT_CHROME_DRIVER():
    DRIVER.close()


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

        # region :- TEST

        '''
        if 'bye' in query:      # Looks for the string 'BYE' in the query.
            print('Exiting..') # Prints out the following string.
            speak("Okay. Bye then!") # Speaks out the given string.
            exit() # Closes the running code.
        '''

        '''
        if 'what' and 'your' and 'name' in query:       # Looks whether the user has asked for its name.
            speak("My name is DOT.")  # Speaks out it's name
        '''

        '''
        if 'what' and 'my' and 'name' in query:
            def what_is_my_name():
                # print('Searching for your name in the stored files...')
                user_name_file_location = pathlib.Path(
                    'C:\\Users\\vivek\\OneDrive\\Desktop\\DHRUV\\Coding\\Python\\DOTa\\Sources\\user_name.txt')
                if user_name_file_location.exists:
                    # print('Found your name in the stored location')
                    user_read_name = user_name_file_location.read_text()
                    speak(f"Your name is {user_read_name} ")
                else:
                    speak("I apologise, I was not able to find your name")

            # Execute the function
            what_is_my_name()
        '''

        '''if 'how are you' in query:
            def user_feeling():
                speak("I'm good. how bout you?")
                print("Good or Bad?")
                feeling = takeCommand().lower()
                feeling_bad_keywords = ["bad", "not", "depressed", "sick"]
                feeling_good_keywords = ["good", "great", "happy"]
                for b in feeling_bad_keywords:
                    # print(b)
                    if b in feeling:
                        speak(
                            "Ohh! That doesn't sound good. I'm here for you, what can I do for you to make you happy")

                for g in feeling_good_keywords:
                    if g in feeling:
                        speak("That is great! Glad to hear that.")

            user_feeling()
        '''

        '''if '+' in query:
            def addition():
                # first_number = int(query[0])
                # second_number = int(query[4])
                # print(first_number)
                # print(second_number)
                # num_sum = first_number + second_number
                # print(num_sum)
                # speak(f"The answer is {num_sum} ")
                res = [int(i) for i in query.split() if i.isdigit()]
                # print(res)
                first_number = int(res[0])
                second_number = int(res[1])
                # print(first_number)
                # print(second_number)
                num_sum = first_number + second_number
                print(num_sum)
                speak(f"The answer is {num_sum} ")

            addition()'''

        # try:
        #     if 'good' in feeling:
        #         speak("Oh that's really cool.")
        #     elif 'great' in feeling:
        #         speak("Nice, glad to hear that")
        #     elif 'not' in feeling:
        #         speak("Oh that's bad to hear")
        #     elif 'bad' in feeling:
        #         speak("Oh that's bad to hear")
        # except Exception as e:
        #     print(e)
        if 'mouse' in query:
            print('Press Ctrl-C to quit.')
            try:
                while True:
                    x, y = pyautogui.position()
                    positionStr = 'X: ' + \
                        str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                    print(positionStr, end='')
                    print('\b' * len(positionStr), end='', flush=True)
            except KeyboardInterrupt:
                print('\n')

# endregion

        # region : SELENIUM

        elif 'spotify' in query:

            if 'log' in query:

                def spotify_login():

                    RUN_CHROME_DRIVER()

                    spotify_credentials_file = open(
                        'Sources\\credentials.json', 'r+')
                    spotify_credentials = json.load(spotify_credentials_file)
                    # print(spotify_credentials)

                    spotify_login_email = spotify_credentials['spotify_email']
                    # print(spotify_login_email)

                    spotify_login_pass = spotify_credentials['spotify_pass']
                    # print(spotify_login_pass)

                    spotify_credentials_file.close()

                    print("Tasks Completed: \n")

                    # open SPOTIFY
                    DRIVER.get('https://open.spotify.com/')
                    print("\t Opened Spotify")
                    speak("Opened Spotify.")
                    # Locating the LOGIN button to start the LOGIN process.
                    login_button = DRIVER.find_element_by_xpath(
                        '/html/body/div[3]/div/div[2]/div[1]/header/div[5]/button[2]')
                    login_button.click()
                    speak('Clicked On Login')
                    print('\t Clicked on Login Button')

                    # Clicking on EMAIL slot and entering the email provided in CREDENTIALS.JSON file.
                    speak("Entering your email")
                    email_slot_spotify = DRIVER.find_element_by_id(
                        'login-username')
                    email_slot_spotify.send_keys(spotify_login_email)
                    print('\t Entered your Email address')

                    # Clicking on PASSWORD slot and entering the password provided in CREDENTIALS.JSON file.
                    speak("Entering your password")
                    password_slot_spotify = DRIVER.find_element_by_id(
                        'login-password')
                    password_slot_spotify.send_keys(spotify_login_pass)
                    print('\t Entered your Password')

                    # Unticking on REMEMBER ME
                    remember_me_button = DRIVER.find_element_by_class_name(
                        'control-indicator')
                    remember_me_button.click()
                    print('\t Unticked Remember Me')

                    # Click on inital LOGIN button

                    login_button = DRIVER.find_element_by_id('login-button')
                    login_button.click()
                    print('\t Clicked on Login')
                    speak("You are now successfully logged in to spotify")

                spotify_login()

            else:
                RUN_CHROME_DRIVER()
                DRIVER.get('https://open.spotify.com/')
                speak("Opened Spotify.")

# endregion
