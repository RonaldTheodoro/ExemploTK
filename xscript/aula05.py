from tkinter import *


root = Tk()

# Titulo da janela principal
root.title('place')

lb = Label(root, text='Hello World')
lb.place(x=100, y=100)

# Tamanho da janela e onde será aberta
root.geometry('300x300+200+200')

root.mainloop()
