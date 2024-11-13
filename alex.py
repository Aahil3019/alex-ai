import pyjokes
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from datetime import date
from requests import get
import cv2
import pywhatkit as kit
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I am ATLAS. Please tell me how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir said: , {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            speak("Sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open song' in query:
            webbrowser.open("spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open code 2' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm 2024.1.1\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'the date' in query:
            today = date.today()
            print(today)
            speak(today)
        elif 'code 3' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip} ")
        elif "send message" in query:
            kit.sendwhatmsg("+919993239853", "Hello, aahil here",18,00)
        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day")
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "shut down" in query:
            os.system("shutdown /s /t 5")
        elif "sleep" in query:
            os.system("rundll32.exe powrprof.dil,SetSuspendState 0,1,0")
        elif "restart" in query:
            os.system("shutdown /r /t 5")

            sys.exit()
        speak("sir, do you have any other work")














