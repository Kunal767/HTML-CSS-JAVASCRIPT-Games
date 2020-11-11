import pyttsx3
import datetime
import speech_recognition
import webbrowser
import os

machine = pyttsx3.init('sapi5')
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id)

def speak(audio):
    machine.say(audio)
    machine.runAndWait()

def wishme():
    timer = int(datetime.datetime.now().hour)
    if timer>0 and timer<12:
        speak("Good Morning Raj Sir")
    elif timer>12 and timer<18:
        speak("Good Afternoon Raj Sir")
    else:
        speak("Good Evening Raj Sir")
    speak("Raj Sir, Komal is Online. Please Tell Me What you want to Do.")

def search():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as pipe:
        print("Say Sentence or Word to Search On Google Sir...")
        speak("Say Sentence or Word to Search On Google Sir...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(pipe, duration=5)
        audio = r.listen(pipe)
    try:
        print("Searching Your Sentence Sir.....")
        speak("Searching Your Sentence Sir.....")
        pipo = r.recognize_google(audio, language='en-in')
        print("You had Said Sir : ", pipo)
        webbrowser.open("https://google.com/?#q=" + pipo)

    except Exception as e:
        print("Say that Again Please Sir....")
        speak("Say that Again Please Sir....")
        return "None"
    return pipo

def search_youtube():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as pipe:
        print("Say Sentence or Word to Search On Youtube Sir...")
        speak("Say Sentence or Word to Search On Youtube Sir...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(pipe, duration=5)
        audio = r.listen(pipe)
    try:
        print("Searching Your Sentence Sir.....")
        speak("Searching Your Sentence Sir.....")
        pipo = r.recognize_google(audio, language='en-in')
        print("You had Said Sir : ", pipo)
        webbrowser.open("https://www.youtube.com/results?search_query=" + pipo)

    except Exception as e:
        print("Say that Again Please Sir....")
        speak("Say that Again Please Sir....")
        return "None"
    return pipo

def takeCmd():
    voiceCatcher = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as inputcmd:
        print("Listening Your Command Sir ....")
        speak("Listening Your Command Sir ....")
        voiceCatcher.pause_threshold = 1
        voiceCatcher.energy_threshold = 1
        voiceCatcher.adjust_for_ambient_noise(inputcmd, duration=2)
        audio = voiceCatcher.listen(inputcmd)
    try:
        print("Recognizing Your Command Sir...")
        speak("Recognizing Your Command Sir...")
        sentence = voiceCatcher.recognize_google(audio, language="en-in")
        print("You had Said Sir " + sentence)
        speak("You had Said Sir " + sentence)
    except:
        print("Sir I am a little bit Deaf, Say that Again Sir....")
        speak("Sir I am a little bit Deaf, Say that Again Sir....")
        return "None"
    return sentence

if __name__ == '__main__':
    wishme()
    while True:
        sentence = takeCmd().lower()

        # Search Methods
        if "search google" in sentence:
            print("Preparing Search Command Wait a Sec Sir...")
            speak("Preparing Search Command Wait a Sec Sir...")
            search()
        elif "search youtube" in sentence:
            print("Preparing Search Command Wait a Sec Sir...")
            speak("Preparing Search Command Wait a Sec Sir...")
            search_youtube()

        # Website Opening
        elif "open youtube" in sentence:
            print("Opening Youtube For You Sir...")
            speak("Opening Youtube For You Sir...")
            webbrowser.open("https://www.youtube.com/")
        elif "open google" in sentence:
            print("Opening Google For You Sir....")
            speak("Opening Google For You Sir....")
            webbrowser.open("https://google.com/")
        elif "open my channel" in sentence:
            print("Opening Your Youtube Channel Sir...")
            speak("Opening Your Youtube Channel Sir...")
            webbrowser.open("https://www.youtube.com/channel/UCLZ3bEbsZKfBZaN7xokPy6Q?view_as=subscriber")

        #     Programs Opening (Path Required)
        #     Uncomment Them and Enter the Path

        # elif "open vs code" in sentence:
        #     print("Opening Visual Studio Code For You Sir...")
        #     speak("Opening Visual Studio Code For You Sir...")
        #     vs_code_path = "vs code ka Path Dedo Double // ke Sath, Ok"
        #     os.open(vs_code_path)

        # elif "open pycharm" in sentence:
        #     print("Opening Pycharm For You Sir....")
        #     speak("Opening Pycharm For You Sir....")
        #     pycharm_path = "pycharm ka path dedo // ke sath, Ok"
        #     os.open(pycharm_path)
