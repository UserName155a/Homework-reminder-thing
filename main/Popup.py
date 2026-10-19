import tkinter as tk
import json
#from tkinter import ttk

userInput = 0;
popUp = None;
labelMemoryLocations: list = [];

def closeBtn():
    root.destroy()

def removeBtnEnd():
    entries["Data"].pop(int(userInput.get())-1);
    popUp.destroy();
    refresh();

def addBtnEnd():
    entries["Data"].append({
                            "taskDue": userInput2.get(),
                            "taskName": userInput.get()
                           });
    popUp.destroy();
    refresh();

def removeBtn():
    global popUp, userInput
    popUp = tk.Tk();
    popUp.wm_attributes("-topmost", True);
    tk.Label(popUp, text = "Remove entry number:").pack();
    userInput = tk.Entry(popUp);
    userInput.pack()
    tk.Button(popUp, text = "Remove", command = removeBtnEnd).pack();

def addBtn():
    global popUp, userInput, userInput2
    popUp = tk.Tk();
    popUp.wm_attributes("-topmost", True);
    tk.Label(popUp, text = "Add task name:").pack();
    userInput = tk.Entry(popUp);
    userInput.pack()
    tk.Label(popUp, text = "Add task due time:").pack();
    userInput2 = tk.Entry(popUp);
    userInput2.pack()
    tk.Button(popUp, text = "Remove", command = addBtnEnd).pack();

userData_Path = "main.json";

def refresh():
    for i in range(0, min(10, len(entries["Data"]))):
        labelMemoryLocations[i].config(text = (str(i+1) + "). " + entries["Data"][i]["taskName"]));
    for i in range(len(entries["Data"]), 10):
        labelMemoryLocations[i].config(text = "");

with open(userData_Path, "r") as file:
    entries = json.loads(file.read());

root = tk.Tk();

root.option_add("*Font", "Monospace 10")

root.geometry("600x400");
root.resizable(False, False);
root.title("Task Check");
root.wm_attributes("-topmost", True);

tk.Label(root, text = "Routine Checkup:", font = ("Noto", 16, "bold")).pack(anchor = "n");
tk.Label(root, text = "To Do:", font = ("Arial", 16)).pack(anchor = "w");

for i in range(0, 10):
    labelMemoryLocations.append(tk.Label(root, text = ""));
    labelMemoryLocations[i].pack(anchor = "w");

    #labelMemoryLocations.append(tk.Label(root, text = (str(i+1) + "). " + entries["Data"][i]["taskName"])));
   # labelMemoryLocations[i].pack(anchor = "w");

refresh();

buttonMenu = tk.Frame(root).pack();
tk.Button(buttonMenu, text = "Close", width = "22", command = closeBtn).pack(side = "left");
tk.Button(buttonMenu, text = "Add", width = "22", command = addBtn).pack(side = "right");
tk.Button(buttonMenu, text = "Remove", width = "22", command = removeBtn).pack(side = "right");

print(labelMemoryLocations);
root.mainloop();
