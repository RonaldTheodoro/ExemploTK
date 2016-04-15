from tkinter import *


root = Tk()

lb1 = Label(root, text='Label 1', width='15', height='3', bg='blue')
lb1.grid(row=0, column=0)

lb2 = Label(root, text='Label 2', bg='red')
lb2.grid(row=1, column=0, sticky=W)

lb3 = Label(root, text='Label 3', bg='yellow')
lb3.grid(row=0, column=1, sticky=S)


root.geometry('250x300+300+300')
root.mainloop()
