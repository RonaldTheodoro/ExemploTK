from functools import partial
from tkinter import *


def bt_click(botao, test):
    print(botao['text'])
    print(test)


root = Tk()

# Titulo da janela principal
root.title('place')

bt1 = Button(root, width=20, text='Botão 1')
bt1['command'] = partial(bt_click, bt1, 'ola1')
bt1.place(x=100, y=100)

bt2 = Button(root, width=20, text='Botão 2')
bt2['command'] = partial(bt_click, bt2, 'ola2')
bt2.place(x=100, y=130)


# Tamanho da janela e onde será aberta
root.geometry('300x300+200+200')

root.mainloop()
