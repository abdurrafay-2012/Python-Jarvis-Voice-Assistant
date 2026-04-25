import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime

# --- Setup Voice ---
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# --- Main Program ---
print("Jarvis is starting...")
speak("Hello Rafay, how can I help you?")

while True:
    # Microphone se sunna
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Voice ko text mein badalna
        command = r.recognize_google(audio).lower()
        print("You said: " + command)

        # 1. Google Open karna
        if "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # 2. YouTube Open karna
        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # 3. Time batana
        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak("The time is " + now)

        # 4. Notepad kholna
        elif "notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        # 5. Program band karna
        elif "stop" in command or "exit" in command:
            speak("Goodbye Rafay!")
            break

    except:
        # Agar awaaz samajh na aaye
        print("Waiting for your voice...")