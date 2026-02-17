import tkinter as tk

class Jarvis:
    def __init__(self, master):
        self.master = master
        self.master.title("Jarvis Voice Assistant")
        self.master.geometry("400x200")

        self.label = tk.Label(master, text="Welcome to Jarvis Voice Assistant!")
        self.label.pack(pady=20)

        self.button = tk.Button(master, text="Speak", command=self.speak)
        self.button.pack(pady=10)

    def speak(self):
        import os
        os.system("echo 'Hello, I am Jarvis. How can I assist you today?' | festival --tts")

if __name__ == '__main__':
    root = tk.Tk()
    jarvis = Jarvis(root)
    root.mainloop()