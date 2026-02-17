import speech_recognition as sr
import pyttsx3

class Jarvis:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            command = ""
            try:
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
            return command

    def run(self):
        self.speak("Hello, I am Jarvis, your voice assistant. How can I help you today?")
        while True:
            command = self.listen()
            if 'exit' in command:
                self.speak("Goodbye!")
                break
            # Add more command processing as needed here

if __name__ == '__main__':
    jarvis = Jarvis()
    jarvis.run()
