from tkinter import *


root = Tk()

lb4 = Label(root, text='Linha 4', bg='red')
lb4.pack(side=RIGHT, fill=BOTH, expand=1)

lb1 = Label(root, text='Linha 1', bg='white')
lb1.pack(side=TOP, fill=BOTH, expand=1)

lb2 = Label(root, text='Linha 2', bg='blue')
lb2.pack(side=TOP, fill=BOTH, expand=1)

lb3 = Label(root, text='Linha 3', bg='yellow')
lb3.pack(side=TOP, fill=BOTH, expand=1)

root.geometry('400x300+300+300')
root.mainloop()
