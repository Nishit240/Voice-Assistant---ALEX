import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

# ---------------- Voice engine (initialized once) ----------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

# ---------------- Voice input ----------------
def sptext():
    """Capture voice input and return as text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("RECOGNIZING...")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}")
            return data
        except sr.UnknownValueError:
            print("Not Understanding The Audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

# ---------------- Voice output ----------------
def speechtx(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

# ---------------- Command processing ----------------
def process_command(command: str, user_name="User") -> str:
    """Process user command and return response"""
    command = command.lower()

    # Exit commands
    exit_words = ["exit", "bye", "tata", "bye-bye", "goodbye"]
    if any(word in command for word in exit_words):
        return "exit_app"  # special flag to signal exit

    # Greetings
    if "hello" in command or "hi alex" in command or "hello alex" in command:
        return "Hello sir, I am Alex your AI assistant"
    if "my name is" in command:
        user_name = command.replace("my name is", "").strip().split(" ")[0]
        return f"Hello {user_name}"

    # General queries
    if "how are you" in command or "how are you today" in command:
        return "I am doing well, thank you for asking. How about you?"
    if "your name" in command:
        return "My name is Alex"
    if "old are you" in command or "your age" in command:
        return "I am 1 year old"
    if "time" in command:
        return datetime.datetime.now().strftime("%I:%M %p")
    if "date" in command:
        return datetime.datetime.now().strftime("%d %B %Y")

    # Websites
    if "chat gpt" in command:
        webbrowser.open("https://chat.openai.com/")
        return "Opening ChatGPT"
    if "w3school for python" in command:
        webbrowser.open("https://www.w3schools.com/python/")
        return "Opening W3Schools Python page"
    if "spotify playlist" in command:
        webbrowser.open("https://open.spotify.com/playlist/7d0r2EppjGw6NDJQPHYz9G?si=fb982bb2ace5433c")
        return "Opening your Spotify playlist"
    if "instagram" in command or "insta" in command:
        webbrowser.open("https://www.instagram.com/")
        return "Opening Instagram"
    if "email" in command or "gmail" in command:
        webbrowser.open("https://www.gmail.com/")
        return "Opening Gmail"
    if "open" in command:
        website_name = command.replace("open", "").strip().split(" ")[0]
        if website_name:
            webbrowser.open(f"https://www.{website_name}.com")
            return f"Opening {website_name}"
        else:
            return "I'm sorry, I didn't catch the website name."

    # Entertainment
    if "play a song" in command:
        webbrowser.open("https://open.spotify.com/track/4nc6XiUze2Yh7wFueGOPv7?si=fb135037fa4842b4")
        return "Playing a song on Spotify"
    if "joke" in command:
        return pyjokes.get_joke(language="en", category="neutral")

    # Photos
    if "my photo" in command:
        add = r"C:\Main files\Education\College\Resume"
        listphoto = os.listdir(add)
        os.startfile(os.path.join(add, listphoto[0]))
        return "Here is your photo"

    # Default
    return "I didn’t understand that. Please try again."
