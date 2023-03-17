from tkinter import *
import time
from random import *
from keyboard import read_key

with open('words.txt', 'r') as file:
    data = file.read()
    words = data.split()


intro = 'This is a typeracer game. Type as fast and accurately as you can. You will be asked for the amount of words you want to be tested on then you will be prompted to press enter to start, after you press enter you may being typing.'


def type_racer():

    def typetest():
        # This function records all the data while typing: time, accuracy etc.
        if start != '':
            print("Error")
        else:
            t0 = time.time()
            inputtext = str(input("Start typing: "))
            t1 = time.time()
            ''' Time ends when you finish typing and click enter'''
            timetaken = round(t1 - t0, 3)
            accuracy = len(set(inputtext.split()) & set(ranwords))
            accuracy = accuracy / wordcount * 100
            wpm = round((wordcount / timetaken) * 60, 2)
            print(f"Time: {timetaken} s Accuracy: {accuracy}% WPM: {wpm}")
    try:
        ''' Try/except block to filter out invalid inputs'''
        print('This is a typeracer game. Type as fast and accurately as you can. You will be asked for the amount of words you want to be tested on then you will be prompted to press enter to start, after you press enter you may being typing.')
        inputwordcount = int(input("How many words do you want to do? 50, 25, or 10: "))
    except ValueError:
        print("Error: Enter valid number")
        type_racer()

    if inputwordcount == 50:
        # 50 word settings
        ranwords = (random.sample(words, 50))
        print(*ranwords, sep=' ')
        wordcount = len(ranwords)
        start = str(input("Click Enter to Start"))
        typetest()
    elif inputwordcount == 25:
        # 25 word setting
        ranwords = (random.sample(words, 25))
        print(*ranwords, sep=' ')
        wordcount = len(ranwords)
        start = str(input("Click Enter to Start"))
        typetest()
    elif inputwordcount == 10:
        # 10 word setting
        ranwords = (random.sample(words, 10))
        print(*ranwords, sep=' ')
        wordcount = len(ranwords)
        start = str(input("Click Enter to Start"))
        typetest()
    else:
        print("Error: Enter valid number (50, 25, or 10)")
        type_racer()



class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Type Racer")
        self.root.resizable(width=False, height=False)

        self.topFrame = Frame(self.root)
        self.botFrame = Frame(self.root)
        self.topFrame.pack()
        self.botFrame.pack()

        self.root.bind("<Key>", self.typingEvent)
        self.root.focus_set()

        # Top Frame
        #self.textFrameCanvas = Canvas(self.topFrame, width=400, height=100, bg="light gray", borderwidth=1, relief="solid")
        #self.textFrameCanvas.pack()
        self.textFrame = Label(self.topFrame, width=50, height=8, borderwidth=1, bg="light gray", relief="solid", text=intro, wraplength=320, anchor='c')
        self.textFrame.bind("<key>")
        self.textFrame.pack(side="left", pady=10,padx=10)


        # Bottom Frame

        self.startButton = Button(self.botFrame, text="Start", command=self.startEvent)
        self.clearButton = Button(self.botFrame, text="Clear", command=self.clearEvent)
        self.exitButton = Button(self.botFrame, text="Exit", command=self.exitEvent)
        self.textEntry = Entry(self.botFrame, bg="light gray", width=35)

        self.textEntry.grid(row=1, column=1, pady=10,padx=10)
        self.startButton.grid(row=1, column=2, pady=10,padx=10)
        self.clearButton.grid(row=1,column=3, pady=10,padx=10)
        self.exitButton.grid(row=1,column=4, pady=10,padx=10)
        
        self.root.mainloop()

    # Display the random words on the screen
    def startEvent(self):
        ranwords = (random.sample(words, 50))
        wordcount = len(ranwords)
        self.textFrame.config(text=ranwords, wraplength=320, anchor='c')
    
    def typingEvent(self):
        def timeStart(self):
            enter = False
            t0 = time.time()
            if read_key =='enter':
                enter = True
            while enter == False:
                t1 = time.time()
            timetaken = round(t1 - t0, 3)
        
        

    def clearEvent(self):
        self.textEntry.delete(0,'end')

    def exitEvent(self):
        self.root.destroy()


def main():
    typeRacer = Gui()

main()
