import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QThread, Signal, QTimer
from alex_voice_assistant import sptext, speechtx, process_command

# ---------------- Voice thread ----------------
class VoiceThread(QThread):
    status_signal = Signal(str)   # LISTENING / RECOGNIZING
    result_signal = Signal(str)   # AI response

    def __init__(self, user_name=None):
        super().__init__()
        self.user_name = user_name

    def run(self):
        # LISTENING
        self.status_signal.emit("LISTENING...")
        command = sptext()

        # RECOGNIZING
        self.status_signal.emit("RECOGNIZING...")

        if command:
            # Handle first-time name introduction
            if not self.user_name and "my name is" in command.lower():
                name = command.lower().replace("my name is", "").strip().split(" ")[0]
                self.user_name = name
                response = f"Nice to meet you, {self.user_name.upper()}!"
            else:
                response = process_command(command, self.user_name)
        else:
            response = "I didn’t understand that. Please try again."

        # If response contains exit signal
        if response.lower() in ["exit_app", "bye", "tata", "bye-bye", "goodbye"]:
            self.result_signal.emit("Goodbye")
            return

        self.result_signal.emit(response)
        speechtx(response)

# ---------------- Frontend UI ----------------
class VoiceUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ALEX")
        self.setFixedSize(400, 600)
        self.setStyleSheet("background-color: #191750;")

        self.mic_on = False
        self.user_name = None

        self.layout = QVBoxLayout()

        # AI Name
        self.name_label = QLabel("ALEX")
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setStyleSheet("font-size:32px; font-weight:bold; color:#d2cde0;")
        self.layout.addWidget(self.name_label)

        # AI Image
        self.top_image = QLabel()
        pixmap = QPixmap(r"C:\Main\Education\PYTHON\project\Voice Assistant\AI.png")
        pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.top_image.setPixmap(pixmap)
        self.top_image.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.top_image)

        # Spacer
        self.layout.addStretch()

        # Big message label
        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setWordWrap(True)
        self.message_label.setStyleSheet("font-size:20px; font-weight:bold; color:#d2cde0;")
        self.layout.addWidget(self.message_label)

        # Dynamic status (LISTENING / RECOGNIZING)
        self.dynamic_label = QLabel("")
        self.dynamic_label.setAlignment(Qt.AlignCenter)
        self.dynamic_label.setWordWrap(True)
        self.dynamic_label.setStyleSheet("font-size:16px; font-weight:bold; color:#d2cde0;")
        self.layout.addWidget(self.dynamic_label)

        # Spacer
        self.layout.addStretch()

        # Mic Status
        self.status_label = QLabel("OFF")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size:12px; color:#d2cde0;")
        self.layout.addWidget(self.status_label)

        # Mic Button
        self.mic_button = QPushButton("🎙️")
        self.mic_button.setFixedSize(60, 60)
        self.mic_button.setStyleSheet("border-radius:20px; background-color:#292574; font-size:30px;")
        self.mic_button.clicked.connect(self.toggle_mic)
        self.layout.addWidget(self.mic_button, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

        # --- First-time greeting AFTER UI shows ---
        QTimer.singleShot(500, self.first_greeting)

    def first_greeting(self):
        if not self.user_name:
            self.message_label.setText("I'm Alex! Can I know your name?")
            speechtx("I'm Alex! Can I know your name?")

    # Toggle mic ON/OFF
    def toggle_mic(self):
        self.mic_on = not self.mic_on
        if self.mic_on:
            self.mic_button.setStyleSheet("border-radius:20px; background-color:#3b45ef; font-size:30px;")
            self.status_label.setText("ON")
            self.start_voice_thread()
        else:
            self.mic_button.setStyleSheet("border-radius:20px; background-color:#292574; font-size:30px;")
            self.status_label.setText("OFF")

    # Start the voice thread
    def start_voice_thread(self):
        self.thread = VoiceThread(user_name=self.user_name)
        self.thread.status_signal.connect(self.update_dynamic_status)
        self.thread.result_signal.connect(self.update_message)
        self.thread.start()

    # Update dynamic status
    def update_dynamic_status(self, text):
        self.dynamic_label.setText(text)

    # Update message and handle exit
    def update_message(self, text):

        # Store name if response is like "Nice to meet you, ..."
        if text.startswith("Nice to meet you"):
            self.user_name = text.split(",")[-1].strip(" !")

        if text == "Goodbye":
            speechtx(f"Goodbye {self.user_name or ''}")
            self.close()
            return
        self.message_label.setText(text)
        self.dynamic_label.setText("")
        self.mic_on = False
        self.mic_button.setStyleSheet("border-radius:20px; background-color:#292574; font-size:30px;")
        self.status_label.setText("OFF")


# ---------------- Run App ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoiceUI()
    window.show()
    sys.exit(app.exec())
