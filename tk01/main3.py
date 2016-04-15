from tkinter import *


class Windown:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(
                frame,
                text='Print Menssage',
                command=self.printMenssege
        )
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='Quit', command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMenssege(self):
        print('wow')


root = Tk()
win = Windown(root)
root.mainloop()
