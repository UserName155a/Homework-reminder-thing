import time
import subprocess
import tkinter as tk
import json

global thresholdTime, Loop;
userInput = 0;
popUp = None;
labelMemoryLocations: list = [];
timerLabel: list = [];
userData_Path = "main/UserData.json";
Loop = True;

with open(userData_Path, "r") as file:
    entries = json.loads(file.read());

start = time.perf_counter()//1; #Inital Time Set
updateTime = 1;
thresholdTime = int(entries["Config"][0]["timerSec"]);

def TimerSettingsUpdate():
    global thresholdTime;
    start = time.perf_counter()//1;
    updateTime = 1;
    thresholdTime = entries["Config"][0]["timerSec"];

# define hell

def PopUp():

    def closeBtn():
        with open(userData_Path, "w") as file:
            json.dump(entries, file, indent = 4);
        root.destroy()

    def removeBtnEnd():
        if str(userInput.get()) == "root":
            permaClose();
            return 0;
        else:
            entries["Data"].pop(int(userInput.get())-1);
            with open(userData_Path, "w") as file:
                json.dump(entries, file, indent = 4);
            popUp.destroy();
            refresh();

    def addBtnEnd():
        entries["Data"].append({
                                "taskDue": userInput2.get(),
                                "taskName": userInput.get()
                            });
        with open(userData_Path, "w") as file:
            json.dump(entries, file, indent = 4);
        popUp.destroy();
        refresh();

    def changeTimerIntEnd():
        global thresholdTime;
        entries["Config"][0]["timerSec"] = max(int(userInput.get()),30);
        with open(userData_Path, "w") as file:
            json.dump(entries, file, indent = 4);
        thresholdTime = entries["Config"][0]["timerSec"];
        timerLabelRefresh();
        popUp.destroy();

    def removeBtn():
        global popUp, userInput
        popUp = tk.Toplevel();
        popUp.wm_attributes("-topmost", True);
        tk.Label(popUp, text = "Remove entry number:").pack();
        userInput = tk.Entry(popUp);
        userInput.pack();
        tk.Button(popUp, text = "Remove", command = removeBtnEnd).pack();

    def addBtn():
        global popUp, userInput, userInput2
        popUp = tk.Toplevel();
        popUp.wm_attributes("-topmost", True);
        tk.Label(popUp, text = "Add task name:").pack();
        userInput = tk.Entry(popUp);
        userInput.pack();
        tk.Label(popUp, text = "Add task due time:").pack();
        userInput2 = tk.Entry(popUp);
        userInput2.pack();
        tk.Button(popUp, text = "Add", command = addBtnEnd).pack();

    def changeTimerInt():
        global popUp, userInput;
        popUp = tk.Toplevel();
        popUp.wm_attributes("-topmost", True);
        tk.Label(popUp, text = "Change interval to (measured in seconds): \nMinimum 30 sec").pack();
        userInput = tk.Entry(popUp);
        userInput.pack();
        tk.Button(popUp, text = "Change", command = changeTimerIntEnd).pack()

    def refresh():
        for i in range(0, min(10, len(entries["Data"]))):
            labelMemoryLocations[i].config(text = (str(i+1) + "). " + entries["Data"][i]["taskName"]));
        for i in range(len(entries["Data"]), 10):
            labelMemoryLocations[i].config(text = "");

    def timerLabelRefresh():
        timerLabel[0].config(text = "popup interval:" + str(thresholdTime) + " seconds");

    def permaClose():
        global Loop;
        Loop = False;
        root.destroy();
    
    root = tk.Tk();
    root.option_add("*Font", "Monospace 10");

    root.geometry("600x400");
    root.resizable(False, False);
    root.title("Task Check");
    root.wm_attributes("-topmost", True);

    tk.Label(root, text = "Routine Checkup:", font = ("Noto", 16, "bold")).pack(anchor = "n");
    tk.Label(root, text = "To Do:", font = ("Arial", 16)).pack(anchor = "w");

    for i in range(0, 10):
        labelMemoryLocations.append(tk.Label(root, text = ""));
        labelMemoryLocations[i].pack(anchor = "w");

    refresh();
    
    buttonMenu = tk.Frame(root);
    buttonMenu.pack(fill = "x");
    buttonSubMenu = tk.Frame(buttonMenu);
    buttonSubMenu.pack(fill = "x");
    tk.Button(buttonSubMenu, text = "Close", command = closeBtn).pack(side = "left", expand = True, fill = "x");
    tk.Button(buttonSubMenu, text = "Add", command = addBtn).pack(side = "left", expand = True, fill = "x");
    tk.Button(buttonSubMenu, text = "Remove", command = removeBtn).pack(side = "left", expand = True, fill = "x");
    tk.Button(buttonMenu, text = "Change popup interval", command = changeTimerInt).pack(fill = "x");

    timerLabel.append(tk.Label(root, text = "popup interval:" + str(thresholdTime) + " seconds"));
    timerLabel[0].pack();

    
    print(labelMemoryLocations);
    root.mainloop();

# Timer

PopUp();
while Loop:
    time.sleep(updateTime);
    TimerSettingsUpdate();
    if ((time.perf_counter())//1 % thresholdTime == 0):
        print("Threshold Reached");
        labelMemoryLocations: list = [];
        timerLabel: list = [];
        PopUp();
