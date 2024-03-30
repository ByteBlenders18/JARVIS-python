import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from gtts import gTTS
from playsound import playsound
import recog_face
import os
import threading
import gui
from features import voice_change


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 1)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        speak("Good Morning!")

    elif (hour >= 12) and (hour < 18):
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am JARVIS , Sir. Please tell me how may I help you")


def speak(audio):
    thread1 = threading.Thread(target=gui.gui_speak)
    # thread2 = threading.Thread(target=assist_fuction.english_assistant)

    thread1.start()
    # thread2.start()
    engine.say(audio)
    engine.runAndWait()
    # thread1.join(timeout=4)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query1 = r.recognize_google(audio, language='en')
        print(f"User said: {query1}\n")
        return query1

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"


def speak_hindi(text):
    var = gTTS(text=text, lang='hi')
    var.save(r"hindisound.mp3")

    # voice_change.male_voice(r"hindisound.mp3")

    playsound(r"hindisound.mp3")

    os.remove(r"hindisound.mp3")

    #
    # os.remove(r"pitchShifted.wav")


def wish_hindi():
    speak_hindi('नमस्ते, मैं JARVIS हूँ, मैं आपके लिए क्या कर सकता हूँ?')


def takeCommand_hindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("बोलिये")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("सुन रही हूँ...")
        query1 = r.recognize_google(audio, language='hi')
        print(f"User said: {query1}\n")
        return query1

    except Exception as e:
        print(e)
        speak("कृपया एक बार फिर से बोलो")
        return "None"


def english_assistant():
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'change to hindi' in query:
            file = open("text/lang.txt", "w")
            file.write("hi")
            file.close()
            hindi_assistant()

        elif "face recog" in query:
            recog_face.recognizer()


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'exit' in query:
            exit()

        # elif "open animation" in query:
        #     os.system("gui.py")

        elif 'change voice to female' in query:
            print("please give voice input")
            voice_input = takeCommand()

            var = gTTS(text=voice_input, lang='hi')
            var.save(r"D:\python projects\Project JARVIS\features\change voice\female_voice.mp3")

            voice_change.female_voice(r"D:\python projects\Project JARVIS\features\change voice\female_voice.mp3")

            playsound(r"D:\python projects\Project JARVIS\features\change voice\pitchShifted_female.wav")


def hindi_assistant():
    wish_hindi()

    while True:
        query_hindi = takeCommand_hindi()

        if 'विकिपीडिया' in query_hindi:
            speak('विकिपीडिया खोज रहा हूँ...')
            query_hindi = query_hindi.replace("विकिपीडिया पर खोजो", "")
            results = wikipedia.summary(query_hindi, sentences=2)
            speak_hindi("विकिपीडिया के अनुसार")
            print(results)
            speak_hindi(results)

        elif 'अंग्रेजी में' in query_hindi:
            file = open("text/lang.txt", "w")
            file.write("en")
            file.close()
            english_assistant()

        elif 'यूट्यूब' in query_hindi:
            webbrowser.open("youtube.com")

        elif 'गूगल खोलो' in query_hindi:
            webbrowser.open("google.com")

        elif 'स्टैकओवरफ़्लो' in query_hindi:
            webbrowser.open("stackoverflow.com")

        elif 'समय' in query_hindi:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak_hindi("सर, समय है")
            speak(f" सर, समय है {strTime}")

        elif 'बंद कर' or 'बंद हो' in query_hindi:
            exit()

