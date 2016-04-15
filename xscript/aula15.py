from tkinter import *


root = Tk()

lb1 = Label(root, text='Label 1')
lb1.grid(row=0, column=0)

lb2 = Entry(root)
lb2.grid(row=0, column=2)

lb3 = Label(root, text='Label 2')
lb3.grid(row=0, column=3)

lb4 = Entry(root)
lb4.grid(row=0, column=4)

lb5 = Label(root, text='Label 3')
lb5.grid(row=1, column=0)

lb6 = Entry(root)
lb6.grid(row=1, column=2)

lb7 = Label(root, text='Label 4')
lb7.grid(row=1, column=3)

lb8 = Entry(root)
lb8.grid(row=1, column=4)

lb9 = Label(root, text='Label 4')
lb9.grid(row=1, column=5)

lb10 = Entry(root)
lb10.grid(row=1, column=6)


root.geometry('650x300+300+300')
root.mainloop()
