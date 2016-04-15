from tkinter import *


root = Tk()

lb1 = Label(root, width='15', height='6', bg='red')
lb1.grid(row=0, column=0)

lb2 = Label(root, width='15', height='6', bg='yellow')
lb2.grid(row=0, column=1)

lb3 = Label(root, width='15', height='6', bg='blue')
lb3.grid(row=1, column=0)

lb4 = Label(root, width='15', height='6', bg='pink')
lb4.grid(row=1, column=1)

lb5 = Label(root, width='10', bg='green')
lb5.grid(row=0, column=2, rowspan=2, sticky=N+S)

lb6 = Label(root, height='5', bg='black')
lb6.grid(row=2, column=0, columnspan=2, sticky=W+E)


root.geometry('500x500+300+300')
root.mainloop()
