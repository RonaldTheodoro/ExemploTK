from tkinter import *


root = Tk()

lb1 = Label(root, text='Nome: ')
lb1.grid(row=0, column=0)

ed1 = Entry(root)
ed1.grid(row=0, column=1)

lb2 = Label(root, text='Senha: ')
lb2.grid(row=1, column=0)

ed2 = Entry(root, show='*')
ed2.grid(row=1, column=1)

bt = Button(root, text='Entrar')
bt.grid(row=2, column=1)

root.geometry('250x100+300+300')
root.mainloop()
