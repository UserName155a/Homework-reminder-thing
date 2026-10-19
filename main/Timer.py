import time
import subprocess

start = time.perf_counter()//1; #Inital Time Set
updateTime = 1; #Seconds
thresholdTime = 3; #Seconds

while True:
    time.sleep(updateTime);
    if (time.perf_counter()//1 % thresholdTime == 0):
        print("Threshold Reached");
        subprocess.Popen(["python", "ToDo Remainder - Typ/Popup.py"])
