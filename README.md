# Tic tac toe
# How do i set it up?
To run the game locally on your PC, you will need to open the release link on the demo button in Macondo, download the .exe file and run it, the game will open(a black screen may appear, didnt know how to fix that) 
# How do i download the exe file of game from the code in Visual Studio code?
Requirements to install:
-Python 3
-PyInstaller
-Downloaded project files
-Internet connection for installing PyInstaller

Steps:
1. Download the project:
   Download or clone this repo and open the project folder.
    Make sure the file containing the game is inside of the folder, then, in the commands below, replace tic_tac_toe.py with the actual       name of the main python file IF IT IS DIFFERENT PLS :)
3. Open a CMD terminal:
   On the terminal, run the following command:
   pip install pyinstaller
   A message should appear if PyInstaller was installed correctly or if it was already downloaded.
4. Build the executable:
   On the terminal, run:
   pyinstaller--onefile--windowed tic_tac_toe.py
   Change tic_tac_toe if necessary (same as before) ONLY DO IF NEEDED PLS :)
   PyInstaller will create several files and folders, including the executable.
5. Find and run the executable:
   After the build finishes, open the project folder and inside of the sub-folder "dist" the .exe file will be there for you to run,         double click to run.
# NOTE:
 If you do not want to follow those instructions, click on the demo button in Macondo to go to the release page of the repo and download the.exe file from there(A black console window MAY appear when downloaded from the release)
# Why did I decide on this project?
 I made this lil game cause im a funny lil fella who likes to make funny lil projects. I made this experiment by using python, and i used functions such as "grid", i also worked on making a functional reset button, for which i used the reset command. I made this project because i want to learn how to code, and also because i was, as we say in Colombia, desparchado :D

# Dev. notes, controls and working functions of the game:
 The game is playable!, player X starts, you need to click to mark a square, includes colors, the playable grid, an easter egg, a reset button to be used at any moment of the match, a visual guide for which player's turn it is, and finally the time i dedicated to this first project, I hope you can enjoy it!!
# Screenshots of working project:
Player X wins:
<img width="1115" height="628" alt="demo" src="https://github.com/user-attachments/assets/f568d713-7a6a-4f6a-9c3c-3194f335ba70" />
Player O wins:
<img width="1115" height="628" alt="demo2" src="https://github.com/user-attachments/assets/c37b7c7d-06e9-41e9-a3bd-a550e438b668" />
