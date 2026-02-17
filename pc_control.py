import os
import subprocess
import pyautogui
import time

class PCControl:
    @staticmethod
    def open_application(app_path: str):
        """Open application at the specified path."""
        subprocess.Popen(app_path)

    @staticmethod
    def control_media(command: str):
        """Control media playback (play, pause, stop)."""
        if command == 'play':
            os.system('xdotool key XF86AudioPlay')  # Linux example
        elif command == 'pause':
            os.system('xdotool key XF86AudioPause')  # Linux example
        elif command == 'stop':
            os.system('xdotool key XF86AudioStop')  # Linux example

    @staticmethod
    def take_screenshot(filename: str):
        """Take a screenshot and save it to the specified filename."""
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)

    @staticmethod
    def manage_task(task_name: str, action: str):
        """Manage system tasks (start, stop)."""
        if action == 'start':
            os.startfile(task_name)
        elif action == 'stop':
            os.system(f'taskkill /f /im {task_name}.exe')  # Windows example

# Example usage:
# PCControl.open_application('C:\Path\To\App.exe')
# PCControl.control_media('play')
# PCControl.take_screenshot('screenshot.png')
# PCControl.manage_task('notepad', 'stop')