import os
import subprocess

class PhoneControl:
    def __init__(self):
        # ADB path should be set if not in environment variables
        self.adb_path = 'adb'

    def send_message(self, phone_number, message):
        command = f'{self.adb_path} shell am start -a android.intent.action.SENDTO -d sms:{phone_number} --es sms_body "{message}" --ez exit_on_sent true'
        subprocess.run(command, shell=True)

    def make_call(self, phone_number):
        command = f'{self.adb_path} shell am start -a android.intent.action.CALL -d tel:{phone_number}'
        subprocess.run(command, shell=True)

    def interact_with_device(self, command):
        subprocess.run(f'{self.adb_path} {command}', shell=True)