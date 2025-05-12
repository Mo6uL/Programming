import time
alarm = input("Set time (HH:MM): ")
while True:
    if time.strftime("%H:%M") == alarm:
        print("ALARM!")
        break
    time.sleep(30)
