from tkinter import *

# Janela
root = Tk()

# Rotulo
# theLabel = Label(root, text='hello world')
# theLabel.pack()

# Frame
# topFrame = Frame(root)
# topFrame.pack()

# Botão
# button = Button(topFrame, text='Button')
# button.pack()

# text: Texto
# fg: Cor das letras
# bg: Cor de fundo
# fill: Tamanho do widget
# .pack(): Mostra o widget na tela

# label_1 = Label(root, text='Name')
# label_2 = Label(root, text='Password')

# Campo de texto
# entry_1 = Entry(root)
# entry_2 = Entry(root)

# Exibe e organiza os itens em uma tabela
# row: define a linha
# column: define a coluna
# columnspan: define quantidade de colunas que vai ocupar
# sticky: define o lado em que o texto fica
# N: norte(topo)
# S: sul(embaixo)
# E: leste(direita)
# W: oeste(esquerda)

# label_1.grid(row=0, sticky=E)
# entry_1.grid(row=0, column=1)
# label_2.grid(row=1, sticky=E)
# entry_2.grid(row=1, column=1)

# Checkbox
# c = Checkbutton(root, text='Keep me logged in')
# c.grid(columnspan=2)


def printname(event):
    print()


# Executar funções
# command: recebe uma função e a executa(não recebe parametros)

button1 = Button(root, text='print')
button1.bind('<Button-1>', printname)
button1.pack()
label = Label(root, text='')
label.pack()

root.mainloop()
