import time
from datetime import datetime
from playsound import playsound
from threading import Thread

exit = False
alarmActive = True

def read_minutes():
    global minutesToClock, minutesToRest
    minutesToClock = float(input("Enter the number of minutes to FOCUS: "))
    minutesToRest = float(input("Enter the number of minutes to REST: "))
    print()

def print_startTime(messageToUser, endOfMessage):
    startTime = datetime.now().strftime("%H:%M")
    print(messageToUser, startTime, end = endOfMessage)

def print_finishTime(endOfMessage = ". "):
    finishTime = datetime.now().strftime("%H:%M")
    print(finishTime, end = endOfMessage)

def print_focus_results():
    print_startTime("Focus: ", " - ")
    time.sleep(minutesToClock * 60)
    print_finishTime()


def print_rest_results():
    print_startTime("Rest: ", " - ")
    time.sleep(minutesToRest * 60)
    print_finishTime()

def printStopAlarm():
    if input("Press any button to stop the alarm. ") == "q":
        global exit
        exit = True
    else: 
        global alarmActive
        alarmActive = False

def play_sound():
    global alarmActive
    while alarmActive and not exit:
        try:
            playsound('./alarmSound.wav')
        except Exception as e:
            print("Error:", e)

def handle_focus():
    print_focus_results()

    # sound of focus alarm
    focus_thread = Thread(target=play_sound, daemon=True)
    focus_thread.start()
    printStopAlarm()
    focus_thread.join()

def handle_rest():
    # sound of rest alarm
    global alarmActive
    alarmActive = True

    print_rest_results()
    rest_thread = Thread(target=play_sound, daemon=True)
    rest_thread.start()

    printStopAlarm()
    rest_thread.join()
    alarmActive = True
    print()

def run():
    handle_focus()
    handle_rest()

def main():
    global exit
    print("\nWelcome to Pomodoro app.\n")
    read_minutes()
    while not exit:
        run()

main()
