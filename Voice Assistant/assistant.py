import pyttsx3
import speech_recognition as sr

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("RECOGNIZING...")
            return recognizer.recognize_google(audio)
        except:
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

def run_assistant():
    """Listen once and return (user_text, alex_reply)."""
    user_text = sptext().lower()

    if "hello alex" in user_text:
        alex_reply = "Hello sir, I am Alex your AI assistant"
    elif "your name" in user_text:
        alex_reply = "My name is Alex"
    elif "bye" in user_text:
        alex_reply = "Goodbye!"
    else:
        alex_reply = "I didn’t understand that."

    speechtx(alex_reply)
    return user_text, alex_reply
