import speech_recognition as sr
import pyttsx3

class VoiceEngine:
    def __init__(self):
        # Initialize the recognizer
        self.recognizer = sr.Recognizer()
        # Initialize the text-to-speech engine
        self.tts_engine = pyttsx3.init()

    def speak(self, text):
        """Convert text to speech."""
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def listen(self):
        """Convert speech to text."""
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")

if __name__ == "__main__":
    voice_engine = VoiceEngine()
    voice_engine.speak("Hello! How can I assist you today?")
    recognized_text = voice_engine.listen()