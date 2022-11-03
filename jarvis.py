# it is an voice module(pyttsx3)
# datetime is also an a module for date and time.
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
# import pypiwin32
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice',voices[0].id)

# creating a function to perform a audio given by user.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning sir.")
    elif hour<=12 and hour<=18:
        speak("Good afternoon sir")
    else:
        speak("Good Evening sir.")
    speak("i am your jarvis, please tell me how may i help you.")


# it takes microphone as a input to understand the user input. 
def takeCommand():
#It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print("Results :",results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new_tab("youtube.com")

        elif 'open google' in query:
            webbrowser.open_new_tab("google.com")
        
        elif 'play music' in query:
            music_dir = 'E:\\songs'
            song = os.listdir(music_dir)
            print("music:",song)
            os.startfile(os.path.join(music_dir, song[0]))
        
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"sir ,the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\Users\cybertech01\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)