import os
import time
import datetime
import psutil
import sys
import signal

def send_notification(message):
    os.system(f"osascript -e 'display notification \"{message}\"'")

def onStart():
    send_notification("TrackApp Program Started!")

def goodbye_notification():
    send_notification("TrackApp terminated. Goodbye!")

def signal_handler(signal, frame):
    goodbye_notification()
    sys.exit(0)

print("\n TrackAPP \n CLI Version \n Author: https://github.com/ajdev05 \n")
time.sleep(1)
print("[+] TrackAPP Running [+] \n")
time.sleep(.5)
def main():

    target_app = input("Enter APP Name: ")
    print(f"\n[+] TrackAPP Tracking [{target_app}]")
    app_running = False
    start_time = None
    onStart()
    while True:
        app_found = any(target_app.lower() in proc.info['name'].lower() for proc in psutil.process_iter(attrs=['pid', 'name']))

        if app_found and not app_running:
            app_running = True
            start_time = datetime.datetime.now()
            send_notification(f"{target_app} opened.")
        elif not app_found and app_running:
            app_running = False
            end_time = datetime.datetime.now()
            duration = end_time - start_time
            send_notification(f"{target_app} closed. Open for {duration}.")
            start_time = None
            print(f"\n[-] TrackAPP Stopped Tracking [{target_app}]")
            return main()
        
        time.sleep(5)  

        

if __name__ == "__main__":
    main()
