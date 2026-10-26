# Homework Reminder Thing

<img src = "/.readme/MainSc.png">

A project for Hack Club Terra

Features:
* A list to store task to do
* The ability to add/remove task
* Easy interval setting

This project is still WIP

Features I plan to add:
* List and sort by task time
* Adjustable list size displayed
* Customizability (Yikes)

How to use:

1 - Install application:
* On Linux: 
    * 1 - Install the executable file 'Main'
    * 2 - run 'cd Downloads' (or the folder you downloaded file into)
    * 3 - run 'chmod +x Main' (it is recommended for you to rename the file, but keeping it as-is is perfectly fine) (this is so you can run from the terminal, but you don't have to, of course)
* On Windows/Mac:
    * 1 - Import the file and folder 'pyproject.toml' and 'main' into a folder and open in an IDE of your choosing (or just cd into the folder you have them in and open terminal from there)
    * 2 - Run the command 'pyinstaller --onefile --add-data "main/UserData.json:main" main/Main.py' and it should create your executable in a folder named 'dist' in the same folder

2 - The buttons
* The 'Close' button
    * It just closes the popup, no drama
* The 'Add' button
    * When clicked, a window will display:

        <img src = "/.readme/AddSc.png">

    * The first field is the name of the task, this is what will be shown on the Main screen
    * The second field doesn't have any real purpose, it does write to the .json file, but the string added is useless... for now
    * The button 'Add' will save your change and it will update the .json and the list on the Main screen
* The 'Remove' button
    * When clicked, a window will display:

        <img src = "/.readme/RemoveSc.png">

    * The field is where you will specify the entry number you want to delete, it is best that you don't try to delete a task you can't see
    * The button 'Remove' will save your change and it will update the .json and the list on the Main screen
* The 'Change popup interval' button
    * When clicked, a window will display:

        <img src = "/.readme/IntervalChangeSc.png>

    * The field is where you will specify the time between each popup, the number you enter is in SECONDS
    * The minimum will be 30 seconds
    * The button 'Change' will save your change and it will update the .json and the list on the Main screen
    * The text below the button will state the current interval
3 - To permamently close the program
* Click on the 'Remove' button and the following should appear:

    <img src = "/.readme/HardStop.png">

* Typing in 'root' and clicking 'Remove' will end the program so it will not bother you again

