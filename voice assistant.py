import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    # Recognizer help to Recognize the voice
    recognizer = sr.Recognizer()

    # Capture the voice through Microphone as source
    with sr.Microphone() as source:
        print("LISTENING...")
        # Removing the noice from voice by using adjust_for_ambient_noise( from source)
        recognizer.adjust_for_ambient_noise(source)
        # the voice is now listen as source
        audio = recognizer.listen(source)

        try:
            print("RECOGNIZING...")
            # Recognize the audio using recognize_google
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understanding The Audio.")
            return ""  # <-- return empty string
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

# # Calling the function
# sptext()
# print("End")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

# # Calling the function
# speechtx("Hello Welcome to your Voice Assistant, My name is ALEX")

if __name__ == '__main__':
    print("Please say 'Hello' to start the voice assistant: ")
    speechtx("Please say Hello")
    count = 0

    while True:
        recognized_text = sptext()
        # Check if the returned text is not None before converting to lowercase
        if recognized_text is not None and recognized_text.lower() == "hello":
            speechtx("hello user")
            speechtx("please say your name")

            while True:
                data1 = sptext().lower()

                if "my name is" in data1:
                    # Extracting the user_name from the voice input
                    user_name = data1.replace("my name is", "").strip().split(" ")[0]
                    speechtx("Hello " + user_name)

                elif "your name" in data1:
                    name = "My name is Alex"
                    speechtx(name)

                elif "old are you" in data1 or "your age" in data1:
                    age = "I am 1 year old "
                    speechtx(age)

                elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)

                elif "date" in data1:
                    time = datetime.datetime.now().strftime("%d%B%Y")
                    speechtx(time)

                elif "chat gpt" in data1:
                    webbrowser.open("https://chat.openai.com/")

                elif "w3school for python" in data1:
                    webbrowser.open("https://www.w3schools.com/python/")

                elif "spotify playlist" in data1:
                    # You can put your spotify playlist by putting the url in the bellow " "
                    webbrowser.open("https://open.spotify.com/playlist/7d0r2EppjGw6NDJQPHYz9G?si=fb982bb2ace5433c")

                elif "w3school for python" in data1:
                    webbrowser.open("https://www.w3schools.com/python/")

                elif "instagram" in data1 or "insta" in data1:
                    webbrowser.open("https://www.instagram.com/")

                elif "email" in data1 or "gmail" in data1:
                    webbrowser.open("https://www.gmail.com/")

                elif "open" in data1:
                    # Extracting the website name from the voice input
                    website_name = data1.replace("open", "").strip().split(" ")[0]

                    # Checking if any website name is provided
                    if website_name:
                        webbrowser.open(f"https://www.{website_name}.com")
                    else:
                        speechtx("I'm sorry, I didn't catch the website name. Please try again.")

                elif "play a song" in data1:
                    # You can put your spotify playlist by putting the url in bellow " "
                    webbrowser.open("https://open.spotify.com/track/4nc6XiUze2Yh7wFueG OPv7?si=fb135037fa4842b4")

                elif "joke" in data1:
                    joke_1 = pyjokes.get_joke(language="en",category="neutral")
                    print(joke_1)
                    speechtx(joke_1)

                elif "my photo" in data1:
                    add = r"C:\Main files\Education\College\Resume"
                    listphoto = os.listdir(add)
                    print(listphoto)
                    os.startfile(os.path.join(add,listphoto[0]))

                elif ("exit" or "bye" or "tata" or "bye-bye") in data1:
                    print(f"Thank You {user_name}")
                    speechtx(f"Thank You {user_name}" )
                    break

                else:
                    print("say something")

                time.sleep(5)

        else:
            print("Please say Hello!!!")
            speechtx("Please say Hallo")
            count =+ 1
            if count == 2:
                print("You have exited:")
                break
            continue


