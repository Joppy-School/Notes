import time
import winsound

ask = input("fast, normal or slow? (F/N/S) ")

pause = 2

ask = ask.upper()

while True:
    if(ask == "F"):
        winsound.Beep(1000, 250)
        time.sleep(pause/4)
    elif(ask == "N"):
        winsound.Beep(1000, 250)
        time.sleep(pause/2)
    elif(ask == "S"):
        winsound.Beep(1000, 250)
        time.sleep(pause)
    else:
        print("Please enter a valid input.")
        break