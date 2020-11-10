'''
My Personal Assistant
Made by ME
Made for ME
'''

# Import packages

import pyttsx3
import speech_recognition as sr
import sys
import datetime
from playsound import playsound
import webbrowser
import youtube_search
import wikipedia
import os
import pathlib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function


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
        print("Listening...")
        r.pause_threshold = 1
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


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        '''Logic for executing tasks based on query'''

        # searches Wikipedia and shows 2 sentences from the summary. Searches Wikipedia only when the user says WIKIPEDIA in the query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

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

        # Opens VS Code
        elif 'open vs code' in query:
            vscode_dir = '"C:\\Users\\vivek\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(vscode_dir)
            speak("Opening VS Code. Code well..")

        # Opens Twitter when the user tells to
        elif 'open twiter' in query:
            webbrowser.open("https://twitter.com/explore")
            speak('Opening Twitter')

        # Opens Hangouts when the user tells to
        elif 'open hangouts' in query:
            webbrowser.open('https://hangouts.google.com/')
            speak('Opening Hangouts')

        # Opens Google when the user tells to
        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')
            speak('Opening Google')

        # Searches Google for the results the user has asked for
        elif 'search google' in query:
            speak("What do I search on Google?")
            Google_Search = takeCommand()
            webbrowser.open(
                "https://google.com/?#q=" + Google_Search)

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
            webbrowser.open('https://github.com/search?q=' + GitHub_Search)

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
            webbrowser.open('https://www.instagram.com/direct/inbox/')
            speak("Opening Instagram DM's")

        # Opens Trello when the user tells to
        elif 'open my note' in query:
            webbrowser.open('https://trello.com/dhruvanand295/boards')
            speak("Opening Trello")

        # Plays music from the directory which has my music
        elif 'play music' in query:
            music_dir = 'C:\\Games'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak('Playing your music')

        # Opens Spotify when the user tells to
        elif 'open spotify' in query:
            spotifyPath = "C:\\Users\\vivek\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifyPath)
            speak('Opening Spotify')

        # Opens My folder [DHRUV] when the user tells to
        elif 'open my folder' in query:
            dhruvFolder = "C:\\Users\\vivek\\OneDrive\\Desktop\\DHRUV"
            os.startfile(dhruvFolder)
            speak('Opened your folder')

        # Opens Hue when the user tells to
        elif 'play hue' in query:
            hueFolder = 'C:\\Users\\vivek\\OneDrive\\Desktop\\DHRUV\\Hue'
            os.startfile(hueFolder)
            speak('Enjoy playing Hue')

        # Opens Zoom to attend class
        elif 'need to attend coaching class' in query:
            zoomFolder = 'C:\\Users\\vivek\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
            os.startfile(zoomFolder)
            speak('Study hard!')

        elif 'attend school classes' in query:
            webbrowser.open(
                'https://classroom.google.com/u/1/?pli=1&authuser=1')
            webbrowser.open('https://web.whatsapp.com/')
            speak("Study properly, all the best")

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

        # CASUAL CONVERSATIONS #

        # Tells the user's name when asked
        elif 'what' and 'my' and 'name' in query:
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

        elif 'what is your name' in query:
            speak("I am Dot. What's your name?")
            user_name = takeCommand()
            speak(f"Nice meeting you {user_name} ")

        elif 'who are you' in query:
            speak("I'm Dot, your Personal Assistant")

        # says it is fine when the user asks about Dot and asks the user about them
        elif 'how are you' in query:
            speak("I'm good. how bout you?")
            print("Good or Bad?")
            feeling = takeCommand().lower()
            not_good_keywords = ["bad", "not", "depressed", "sick"]
            feeling_good_keywords = ["good", "great", "happy"]
            for b in not_good_keywords:
                # print(b)
                if b in feeling:
                    speak(
                        "Ohh! That doesn't sound good. I'm here for you, what can I do for you to make you happy")

            for g in feeling_good_keywords:
                if g in feeling:
                    speak("That is great! Glad to hear that.")

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
