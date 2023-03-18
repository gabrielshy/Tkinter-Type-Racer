'''
Creator: Francis Gabriel Anos
Project Title: Tkinter Type Racer Game

Version 3.0 changes:
Improved system so that whenever you click enter after finishing
the game, the game doesn't reset your stats as it did before.

Allowed the entry box to be disabled after clicking enter

Fixed typos

Fixed WPM
'''

from tkinter import *
import time
import random
import keyboard as kb

# Importing a txt document with a random assortment of words and numbers
with open('words.txt', 'r') as file:
    data = file.read()
    words = data.split()

# Intro for the game; displayed at the start screen
intro = 'This is a typeracer game. Type as fast and accurately as you can. After clicking the "start" button, ' \
        'you will be shown 30 words or numbers. The moment you start typing, the timer will start, ' \
        'and when you click enter, the timer will end.'


class Gui:
    def __init__(self):
        # Creating the Tkinter GUI
        self.root = Tk()
        self.root.title("Type Racer")
        self.root.resizable(width=False, height=False)

        self.topFrame = Frame(self.root)
        self.botFrame = Frame(self.root)
        self.topFrame.pack()
        self.botFrame.pack()

        # Allows the application to detect what keys you input
        self.root.bind("<Key>", self.typingEvent)
        self.root.focus_set()

        # Top Frame

        self.textFrame = Label(self.topFrame, width=50, height=8, borderwidth=1, bg="light gray", relief="solid",
                               text=intro, wraplength=320, anchor='center')
        self.textFrame.bind("<key>")
        self.textFrame.pack(side="left", pady=10, padx=10)

        # Bottom Frame

        self.startButton = Button(self.botFrame, text="Start", command=self.startEvent)
        self.clearButton = Button(self.botFrame, text="Clear", command=self.clearEvent)
        self.exitButton = Button(self.botFrame, text="Exit", command=self.exitEvent)

        self.startButton.grid(row=1, column=2, pady=10, padx=10)
        self.clearButton.grid(row=1, column=3, pady=10, padx=10)
        self.exitButton.grid(row=1, column=4, pady=10, padx=10)

        self.root.mainloop()

    # Display the random words on the screen
    def startEvent(self):
        # Set 'ranwords' to global in order to use the current set of words everywhere
        global ranwords, checkEnter

        checkEnter = True
        # When clicking start, the GUI will show the entry box for the user
        self.textEntry = Entry(self.botFrame, bg="light gray", width=35, state='normal')
        self.textEntry.grid(row=1, column=1, pady=10, padx=10)

        # Pulling a random sample of words from words.txt
        ranwords = (random.sample(words, 30))

        # 'Wordset' is the list 'ranwords' without the brackets and commas
        wordset = ' '.join(str(x) for x in ranwords)
        self.textFrame.config(text=f"Start typing:\n"
                                   f"{wordset}", wraplength=320, anchor='center')
        self.root.mainloop()

    # 'typingEvent' is the function that holds the actions after starting the game
    def typingEvent(self, t1=float):
        # Set 'start' to global in order to make the entire game connected just in
        # case the user clicks clear and wants to start over. Set 't0' to global in order to
        # make the start time across the entire game consistent
        global t0, start, checkEnter

        # if statement checks to see if this is the start of the game
        if start:
            t0 = time.time()

            # after the timer starts, start bool is set to False unless clearEvent is clicked
            start = False

        if checkEnter:
            # When 'enter' is clicked on the keyboard, the game ends and the stats appear
            if kb.read_key() == 'enter':
                # FIXED Ver 3.0: Make the entry box and key inputs disabled after clicking enter
                self.textEntry.config(state='disabled')
                checkEnter = False
                t1 = time.time()

                # Setting 'start' to True so that a new game can be started
                start = True

                # Stats section:
                timetaken = round(t1 - t0, 3)
                words = self.textEntry.get().split(" ")
                accuracy = len(set(words) & set(ranwords))
                accuracy = accuracy / len(words) * 100
                # Grade is based on your accuracy
                if 100 >= accuracy >= 90:
                    grade = 'A'
                elif 89.9 >= accuracy >= 80:
                    grade = 'B'
                elif 79.9 >= accuracy >= 70:
                    grade = 'C'
                elif 69.9 >= accuracy >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                self.textFrame.config(text=f"Stats:\n"
                                           f"Time: {timetaken} seconds\n"
                                           f"Words: {len(words)}\n"
                                           f"WPM: {round(len(words) / timetaken  * 60, 3)}\n"
                                           f"Accuracy: {round(accuracy, 3)}%\n"
                                           f"Grade: {grade}")
                self.clearButton.config(text="Restart")
                self.root.mainloop()

    # Clear event is when the user wants to clear their entry box. The clear event is also used to
    # restart the game when the game is finished.
    def clearEvent(self):
        # Set 'start' to global in order to keep start consistent
        global start, checkEnter

        # clearButton checks if clearButton text is 'clear' or 'restart'
        clearButton = self.clearButton.cget('text')
        if clearButton == "Clear":
            self.textEntry.delete(0, 'end')
            checkEnter = True
            start = True

        # If it is restart, the window is destroyed, and a new game opens
        if clearButton == "Restart":
            self.root.destroy()
            Gui()

    # Exit button
    def exitEvent(self):
        self.root.destroy()

# Main starts the Tkinter GUI
def main():
    global start
    start = True
    Gui()


main()
