from tkinter import *


def bt_click():
    print('bt_click')
    lb['text'] = 'oi'

root = Tk()

# Titulo da janela principal
root.title('place')

bt = Button(root, width=20, text='OK', command=bt_click)
bt.place(x=100, y=150)

lb = Label(root, text='Hello World')
lb.place(x=100, y=100)

# Tamanho da janela e onde será aberta
root.geometry('300x300+200+200')

root.mainloop()
