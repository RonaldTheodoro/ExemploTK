from tkinter import *


root = Tk()
# Anchor (N, S, CENTER, W, L, NW, NE, SW, SE)

lb1 = Label(root, text='Label1', bg='WHITE')
lb1.pack(anchor=N)
lb2 = Label(root, text='Label2', bg='WHITE')
lb2.pack(anchor=S)
lb3 = Label(root, text='Label3', bg='WHITE')
lb3.pack(anchor=E)
lb4 = Label(root, text='Label4', bg='WHITE')
lb4.pack(anchor=W)
lb5 = Label(root, text='Label5', bg='WHITE')
lb5.pack(anchor=NE)
lb6 = Label(root, text='Label6', bg='WHITE')
lb6.pack(anchor=NW)
lb7 = Label(root, text='Label7', bg='WHITE')
lb7.pack(anchor=SE)
lb8 = Label(root, text='Label8', bg='WHITE')
lb8.pack(anchor=SW)
lb9 = Label(root, text='Label9', bg='WHITE')
lb9.pack(anchor=CENTER)


root['bg'] = 'BLACK'
root.geometry('400x300+300+300')
root.mainloop()
