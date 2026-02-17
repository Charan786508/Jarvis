# Jarvis - Personal Voice Assistant

A simple and lightweight voice assistant designed to help you operate and control your phone and PC using voice commands.

## Features

- 🎤 **Voice Recognition** - Understands natural voice commands
- 💻 **PC Control** - Open applications, browse files, control media
- 📱 **Phone Integration** - Control smartphone functionalities
- 🤖 **Automation** - Automate repetitive tasks
- ⚙️ **Easy Configuration** - Simple setup and customization

## Prerequisites

- Python 3.8+
- Microphone (for voice input)
- Internet connection (for speech recognition)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Charan786508/Jarvis.git
cd Jarvis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Start Jarvis:
```bash
python jarvis.py
```

## Supported Commands

### PC Control
- "Open [application name]" - Open an application
- "Search [query]" - Search on Google
- "Play music" - Open media player
- "Take screenshot" - Capture screen
- "Shutdown" - Shutdown the system

### Phone Control
- "Send message" - Send SMS/Messages
- "Make call" - Initiate a call
- "Get location" - Share location

## Project Structure

```
Jarvis/
├── jarvis.py           # Main application file
├── requirements.txt    # Python dependencies
├── config.py          # Configuration settings
├── voice_engine.py    # Voice recognition module
├── pc_control.py      # PC automation module
├── phone_control.py   # Phone control module
└── README.md          # Documentation
```

## Technologies Used

- **Speech Recognition** - pyttsx3, SpeechRecognition
- **Automation** - pyautogui, subprocess
- **Phone Control** - ADB (Android Debug Bridge)
- **GUI** - Tkinter

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Author

**Charan786508** - [GitHub Profile](https://github.com/Charan786508)

---

**Note:** This is an active development project. More features coming soon!