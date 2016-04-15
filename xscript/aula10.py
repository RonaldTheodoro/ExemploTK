from tkinter import *


root = Tk()
# Side (TOP, BOTTOM, LEFT, RIGHT)

lb1 = Label(root, text='Label 1', bg='blue')
lb1.pack(side=TOP)
lb2 = Label(root, text='Label 2', bg='red')
lb2.pack(side=BOTTOM)
lb3 = Label(root, text='Label 3', bg='green')
lb3.pack(side=LEFT)
lb4 = Label(root, text='Label 4', bg='yellow')
lb4.pack(side=RIGHT)

root.geometry('400x300+300+300')
root.mainloop()
