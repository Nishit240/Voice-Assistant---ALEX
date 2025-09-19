# Voice Assistant - ALEX 🎙️

This Python script implements a versatile voice assistant named ALEX, featuring voice recognition, text-to-speech capabilities, and various functionalities. ALEX responds to voice commands, providing information, opening websites, and executing tasks based on user input.

## Features 🌟

- **Voice Recognition**: Utilizes the `speech_recognition` library to accurately recognize voice commands.
- **Text-to-Speech**: Employs the `pyttsx3` library to convert textual responses into natural-sounding speech.
- **Functionality**:
  - Greeting the user and prompting for their name.
  - Answering basic questions about itself.
  - Providing the current time and date.
  - Opening specified websites, including Spotify, Google,Facebook, YouTube, Instagram, Gmail and more.
  - Playing a song on Spotify.
  - Sharing a random joke using the `pyjokes` library.
  - Displaying the user's photo stored in a specified directory.

## Prerequisites ⚙️

- Python 3.x
- Install the required Python packages:

  ```bash
  pip install pyttsx3
  pip install SpeechRecognition
  pip install pyaudio
  pip install webbrowser
  pip install pyjokes
  pip install pyside6  
  ```

## Screenshot 🖼️
<img width="519" height="811" alt="Screenshot 2025-09-19 160214" src="https://github.com/user-attachments/assets/c76c5e42-012a-4d12-956e-bc60286e9d4c" />

<img width="516" height="799" alt="Screenshot 2025-09-19 160224" src="https://github.com/user-attachments/assets/cad5353e-4ae1-4778-b20b-7789273017fc" />

<img width="1435" height="1077" alt="Screenshot 2025-09-19 160310" src="https://github.com/user-attachments/assets/790dcdd8-be84-4661-a39e-6420e91e2c56" />

<img width="1460" height="1079" alt="Screenshot 2025-09-19 160345" src="https://github.com/user-attachments/assets/0ddc47b7-40d5-4173-8f00-1eda765e71f9" />


## Usage 🚀

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/voice-assistant.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd alex_voice-assistant
    ```

3. **Run the script:**

    ```bash
    python alex_voice_assistant.py
    ```

4. **Follow the on-screen instructions and say "HEY ALEX" to initiate the voice assistant.**

## Configuration ⚙️

- Customize ALEX's behavior by modifying the conditions within the `while True` loop in the code.
- Update the Spotify playlist URL and photo directory paths as needed.


## Author 🧑‍💻

- [Nishit]
- [nishitjain02419@gmail.com]

## Disclaimer ⚠️

This voice assistant is a basic implementation and may require additional improvements for production use. Use it at your own discretion.
