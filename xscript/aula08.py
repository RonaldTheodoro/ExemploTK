from tkinter import *


def bt_onclick():
    lb['text'] = ed.get()


root = Tk()

ed = Entry(root)
ed.place(x=100, y=100)

bt = Button(root, width=20, text='OK', command=bt_onclick)
bt.place(x=100, y=130)

lb = Label(root, text='Label')
lb.place(x=100, y=200)

root.geometry('300x300+300+300')
root.mainloop()
