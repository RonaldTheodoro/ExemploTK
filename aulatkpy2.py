# -*- coding:utf-8 -*-
import sqlite3
import tkMessageBox
from Tkinter import *


class Main:

    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.pack()
        Label(self.frame, text='Digite sua nota').pack()
        self.nota = Entry(self.frame, width=35)
        self.nota.pack()
        self.separador = Frame(height=2, width=100, bd=3, relief=SUNKEN)
        self.separador.pack(fill=X, padx=5, pady=5)
        self.frame3 = Frame(root)
        self.frame3.pack()
        self.add = Button(
                self.frame3,
                text='Adicionar nota',
                command=self.adicionar
        )
        self.add.pack(side=LEFT)
        self.apagar = Button(
                self.frame3,
                text='Apagar nota',
                command=self.apagar
        )
        self.apagar.pack(side=LEFT)
        scrollbar = Scrollbar(root)
        scrollbar.pack(fill=Y, side=RIGHT)
        self.listbox = Listbox(root, width=50, height=20)
        self.listbox.pack(padx=5, pady=5)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Cria banco de dados
        self.conectar = sqlite3.connect('notas.db')
        self.cursor = self.conectar.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS notas(name TEXT)')
        self.conectar.commit()
        lista = self.cursor.execute('SELECT * FROM notas')
        for i in lista:
            self.listbox.insert(END, i)

    def adicionar(self):
        notax = self.nota.get()
        if notax == '':
            tkMessageBox.showwarning('Erro', 'Insira uma nota')
        else:
            self.cursor.execute('INSERT INTO notas VALUES(?)', (notax,))
            self.conectar.commit()
            self.listbox.insert(END, notax)
            self.nota.delete(0, END)

    def apagar(self):
        notay = str(self.listbox.get(ACTIVE))[3:-3]
        self.cursor.execute('DELETE FROM notas WHERE name = ?', (notay,))
        self.conectar.commit()
        self.listbox.delete(ANCHOR)


def fechar():
    titulo = 'Fechar a aplicação'
    msg = 'Você realmente deseja fechar o aplicativo'
    if tkMessageBox.askyesno(titulo, msg):
        exit()
    else:
        pass

root = Tk()
root.title('Minhas notas')
root.geometry('300x400')
root.protocol('WM_DELETE_WINDOW', fechar)
Main(root)

root.mainloop()
