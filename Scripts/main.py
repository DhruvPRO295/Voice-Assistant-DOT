'''
My Personal Assistant
Made by ME
Made for ME
'''

# Import packages

import pyttsx3
from gtts import gTTS
import speech_recognition as sr
import sys
import datetime
import time
import playsound
import webbrowser
import youtube_search
import wikipedia
import os
import json
import pathlib
from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


# Speak function

# GTTS
# def say(text):
#     tts = gTTS(text=text, lang="en")
#     filename = 'voice.mp3'
#     tts.save(filename)
#     playsound.playsound(filename)


''' Useful Functions '''

# Function to Open the CHROME DRIVE only when asked for.


def RUN_CHROME_DRIVER():
    global DRIVER
    DRIVER = webdriver.Chrome(
        executable_path='C:\\Program Files (x86)\\Selenium\\chromedriver.exe')
    global DRIVER_ACTION
    DRIVER_ACTION = ActionChains(DRIVER)


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


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function which wishes the user based on the time of the day


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Dot. Please tell me how may I help you?")

# takeCommand function


def takeCommand():
    # Takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        wake_sound = 'Sources\\wake_sound.mp3'
        playsound.playsound(wake_sound)
        print("Listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)

        print('Say that again please.')
        return "None"
    return query

# Chrome DRIVER for Automation.

# DRIVER_PATH = 'C:\\Program Files (x86)\\chromium\\chromedriver.exe'
# driver = webdriver.Chrome(DRIVER_PATH)


if __name__ == "__main__":

    # Wishes the user upon starting the Voice Assistant.
    # wishMe()
    while True:
        query = takeCommand().lower()

        # This is the WAKE_KEYWORD for which the Voice Assistant will listen for.
        # WAKE_KEYWORD = ["hi dot", "hey dot", "okay dot", "ok dot"]
        # for WAKE in WAKE_KEYWORD:
        #     if WAKE in query:
        #         # If the user has said the WAKE_KEYWORD more than 0 times then it will listen for further query.
        #         if query.count(WAKE) > 0:
        #             speak("I\'m listening")
        #             print("I'm listening")
        #             query = takeCommand().lower()

        '''Logic for executing tasks based on query'''

        # searches Wikipedia and shows 2 sentences from the summary. Searches Wikipedia only when the user says WIKIPEDIA in the query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            wikipedia_query = query.replace("Wikipedia", "")
            wikipedia_results = wikipedia.summary(
                wikipedia_query, sentences=2)
            speak('According to Wikipedia')
            print(wikipedia_results)
            speak(wikipedia_results)

        # if the user says "Do not" in their phrase then Dot says it won't do it :)
        elif 'do not' in query:
            speak("Okay I won't do it.")

        # Opens YouTube when the user tells to
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak('Opening YouTube')

        # searches YouTube for the result the user asked for
        elif 'search youtube' in query:
            speak("What do I search on YouTube?")
            YT_Search = takeCommand()
            webbrowser.open(
                "https://www.youtube.com/results?search_query=" + YT_Search)

        # Searches for the requested vidoe on YouTube
        elif 'on' and 'youtube' in query:
            YT_Search = query.replace("search", "")
            YT_Search = YT_Search.replace(" for ", "")
            YT_Search = YT_Search.replace("on", "")
            YT_Search = YT_Search.replace("youtube", "")
            webbrowser.open(
                'https://www.youtube.com/results?search_query=' + YT_Search)
            speak(f"Searching for {YT_Search} on YouTube.")

        # Opens VS Code
        elif 'open' and 'vs code' in query:
            vscode_dir = '"C:\\Users\\vivek\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(vscode_dir)
            speak("Opening VS Code. Code well..")

        # Opens Twitter
        elif 'open' and 'twiter' in query:
            webbrowser.open("https://twitter.com/explore")
            speak('Opening Twitter')

        # Opens Hangouts
        elif 'open hangouts' in query:
            webbrowser.open('https://hangouts.google.com/')
            speak('Opening Hangouts')

        # Opens Google
        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')
            speak('Opening Google')

        # Searches Google for the results the user has asked for
        elif 'search google' in query:
            speak("What do I search on Google?")
            Google_Search = takeCommand()
            webbrowser.open(
                "https://google.com/?#q=" + Google_Search)

        # Searches Google
        elif 'on' and 'google' in query:
            google_voice_search = query.replace("find", "")
            google_voice_search = google_voice_search.replace(
                "search", "")
            google_voice_search = google_voice_search.replace(
                "on", "")
            google_voice_search = google_voice_search.replace(
                "for", "")
            google_voice_search = google_voice_search.replace(
                "google", "")
            speak(f"Searching Google for {google_voice_search}")
            webbrowser.open(
                'https://google.com/?#q=' + google_voice_search)

        # Opens GitHUb Desktop
        elif 'open github desktop' in query:
            github_desktop_dir = 'C:\\Users\\vivek\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe'
            os.startfile(github_desktop_dir)
            speak("opening GitHub Desktop")

        # Opens GitHub when the user tells to
        elif 'open github' in query:
            webbrowser.open('https://github.com/')
            speak('Opening GitHub')

        # Searches GitHub for repositories
        elif 'search github' in query:
            speak('What do I search on GitHub?')
            GitHub_Search = takeCommand()
            webbrowser.open(
                'https://github.com/search?q=' + GitHub_Search)

        # Opens Whatsapp when the user tells to
        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')
            speak('Opening Whatsapp')

        # Opens Google Classroom app
        elif 'open classroom' in query:
            webbrowser.open(
                'https://classroom.google.com/u/1/?pli=1&authuser=1')
            speak("Opening Classroom")

        # Opens Instagram when the user tells to
        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com/')
            speak('Opening Instagram')

        # Opens Instagram DM for messaging and viewing messages
        elif 'instagram dm' in query:
            webbrowser.open(
                'https://www.instagram.com/direct/inbox/')
            speak("Opening Instagram DM's")

        # Opens Trello when the user tells to
        elif 'open' and 'trello' and 'note' in query:
            webbrowser.open(
                'https://trello.com/dhruvanand295/boards')
            speak("Opening Trello")

        # Plays music from the directory which has my music
        elif 'play music' in query:
            music_dir = 'C:\\Games'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak('Playing your music')

        # SPOTIFY
        elif 'spotify' in query:

            if 'open' in query:
                RUN_CHROME_DRIVER()

                DRIVER.get('https://open.spotify.com/')
                speak('Opening Spotify')
                print('Opened Spotify')
                speak("Do you wish to login first?")
                spotify_login_query = takeCommand().lower()
                if 'ye' in spotify_login_query:
                    speak("Okay I will log you in.")
                    spotify_login()
                else:
                    print("You will have to manually login.")
                    DRIVER.get('https://open.spotify.com/')

            elif 'log' in query:
                spotify_login()

            elif 'on' and 'spotify' in query:
                RUN_CHROME_DRIVER()
                # Searches for the requested track on Spotify
                # Replace all other strings from the QUERY and just leave the song name.
                spotify_song_name = query.replace("search", "")
                spotify_song_name = spotify_song_name.replace(
                    "play", "")
                spotify_song_name = spotify_song_name.replace(
                    "for", "")
                spotify_song_name = spotify_song_name.replace(
                    " on ", "")
                spotify_song_name = spotify_song_name.replace(
                    "spotify", "")
                print(f"Searching for {spotify_song_name} on Spotify")
                # Open the URL and add the SONG NAME in the end to search for the requested song.
                DRIVER.get('https://open.spotify.com/search/' +
                           spotify_song_name)
                # Check if the user want's to PLAY the song.
                if 'play' in query:
                    spotify_song_play_button = DRIVER.find_element_by_xpath(
                        '/html/body/div[4]/div/div[2]/div[4]/main/div[2]/div[2]/div/div/div[2]/div/div/div/section[1]')
                    spotify_song_play_button.click()
                    speak(
                        f"Okay! Playing {spotify_song_name} on Spotify")
                # If the user doesn't say "PLAY" in the QUERY then it will just search for the song.
                else:
                    speak('Here is the track you asked for.')

            else:
                RUN_CHROME_DRIVER()
                DRIVER.get('https://open.spotify.com/')
                speak("Opened Spotify.")

        # # Opens Spotify when the user tells to
        # elif 'open spotify' in query:
        #     spotifyPath = "C:\\Users\\vivek\\AppData\\Roaming\\Spotify\\Spotify.exe"
        #     os.startfile(spotifyPath)
        #     speak('Opening Spotify')

        # Opens My folder [DHRUV] when the user tells to
        elif 'open my folder' in query:
            dhruvFolder = "C:\\Users\\vivek\\OneDrive\\Desktop\\DHRUV"
            os.startfile(dhruvFolder)
            speak('Opened your folder')

        # Tells the time when user asks
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")

        # Sets an alarm at the specified time
        elif 'set an alarm' in query:
            speak("What hour do you want to set the alarm for?")
            alarm_hour = int(takeCommand())
            speak("What minutes do you want to set the alarm for?")
            alarm_minutes = int(takeCommand())
            speak("Alarm has been set")
            print("Waiting for alarm", alarm_hour, alarm_minutes, )
            while True:
                if(alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute):
                    print("Wake up!")
                    speak("Hey there. It's time!")
                    break

        # MATHEMATICAL OPERATIONS

        # Addition of two integers
        elif '+' and 'plus' in query:
            def addition():
                res = [int(i)
                       for i in query.split() if i.isdigit()]
                first_number = int(res[0])
                second_number = int(res[1])
                num_sum = first_number + second_number
                print(num_sum)
                speak(f"The answer is {num_sum} ")

            # Execute the function
            addition()

        # CASUAL CONVERSATIONS #

        # Replies when the user tells hello.
        elif 'hello' in query:
            speak("Hello there")

        # Tells the user's name when asked
        elif 'what' and 'name' and 'my' in query:
            def what_is_my_name():
                # print('Searching for your name in the stored files...')
                user_name_file_location = pathlib.Path(
                    'C:\\Users\\vivek\\OneDrive\\Desktop\\DHRUV\\Coding\\Python\\DOTa\\Sources\\user_name.txt')
                if user_name_file_location.exists:
                    # print('Found your name in the stored location')
                    user_read_name = user_name_file_location.read_text()
                    speak(f"Your name is {user_read_name} ")
                else:
                    speak(
                        "I apologise, I was not able to find your name")

            # Execute the function
            what_is_my_name()

        elif 'what' and 'name' and 'your' in query:
            speak("I am Dot.")

        elif 'who are you' in query:
            speak("I'm Dot, your Personal Assistant")

        # says it is fine when the user asks about Dot and asks the user about them
        elif 'how are you' in query:
            def user_feeling():
                speak("I'm good. how bout you?")
                print("Good or Bad?")
                feeling = takeCommand().lower()
                feeling_bad_keywords = [
                    "bad", "not", "depressed", "sick"]
                feeling_good_keywords = ["good", "great", "happy"]
                for b in feeling_bad_keywords:
                    # print(b)
                    if b in feeling:
                        speak(
                            "Ohh! That doesn't sound good. I'm here for you, what can I do for you to make you happy")

                for g in feeling_good_keywords:
                    if g in feeling:
                        speak("That is great! Glad to hear that.")

            # Execute the code
            user_feeling()

        # Becomes happy when the user tells "THANK YOU"
        elif 'thank' in query:
            speak("I'm pleased to help you!")
            print('( ͡° ͜ʖ ͡°)')

        # Exits the program when the user says 'BYE'
        elif 'bye' in query:
            speak("Until next time")
            exit()
            sys.exit()

        # Exits the program when the user says 'see you later'
        elif 'see you later' in query:
            speak("Okay come back soon")
            exit()
            sys.exit()
