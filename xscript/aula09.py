from tkinter import *


def soma():
    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        lb['text'] = int(ed1.get()) + int(ed2.get())
    else:
        lb['text'] = 'Erro'

root = Tk()

ed1 = Entry(root)
ed1.place(x=100, y=100)

ed2 = Entry(root)
ed2.place(x=100, y=120)

bt = Button(root, text='Soma', command=soma)
bt.place(x=100, y=140)

lb = Label(root, text='')
lb.place(x=100, y=180)

root.geometry('400x300+300+300')
root.mainloop()
