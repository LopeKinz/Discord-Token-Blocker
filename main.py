import os
import time
import psutil

def monitor_token_file():
    discord_token_path = "path/to/discord/token/file"

    while True:
        for proc in psutil.process_iter(attrs=['name']):
            if proc.info['name'].lower() not in ['discord.exe', 'chrome.exe']:
                try:
                    open_files = proc.open_files()
                except psutil.AccessDenied:
                    continue

                for file in open_files:
                    if file.path == discord_token_path:
                        print("Unauthorized program tried to access the Discord token file!")
                        print("Blocking access...")
                        os.system("taskkill /pid " + str(proc.pid))

        time.sleep(5)

monitor_token_file()
