from tkinter import *


root = Tk()

lb1 = Label(root, text='Label', bg='red')
lb1.pack(side=TOP, fill=X)

lb2 = Label(root, text='', bg='black')
lb2.pack(side=LEFT, fill=Y)

lb3 = Label(root, text='', bg='black')
lb3.pack(side=RIGHT, fill=Y)

root.geometry('400x300+300+300')
root.mainloop()
