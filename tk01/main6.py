import sys
from tkinter import *
from tkinter import messagebox


class TKGui:

    def __init__(self, root):
        self.root = root

    def menuConfig(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.option = Menu(self.menu)
        self.menu.add_cascade(label='Opções', menu=self.option)
        self.option.add_command(label='Sair', command=close)

        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label='Ajuda', menu=self.helpmenu)
        self.helpmenu.add_command(label='Sobre', command=showversion)

    def infoStore(self):
        self.info = Frame(self.root, width=600, height=800)
        self.info.grid()

    def infoLabel(self):
        self.code = Label(self.info, text='Codloja')
        self.code.grid(column=0, row=0, sticky=W)
        self.store = Label(self.info, text='Loja')
        self.store.grid(column=2, row=0, sticky=W)
        self.ramal = Label(self.info, text='Ramal')
        self.ramal.grid(column=3, row=0, sticky=W)
        self.phone = Label(self.info, text='Telefone')
        self.phone.grid(column=0, row=3, sticky=W)
        self.address = Label(self.info, text='Endereço')
        self.address.grid(column=0, row=4, sticky=W)
        self.grife = Label(self.info, text='Grife')
        self.grife.grid(column=0, row=5, sticky=W)
        self.supervisor = Label(self.info, text='Supervisor')
        self.supervisor.grid(column=0, row=6, sticky=W)
        self.cnpj = Label(self.info, text='CNPJ')
        self.cnpj.grid(column=0, row=7, sticky=W)

    def pingBox(self):
        self.pingbox = Frame(self.info, width=600, height=600)
        self.pingbox.grid()


def close():
    sys.exit(0)


def showversion():
    messagebox.showinfo(
            'Sobre o Numeron Network',
            'Versão 2.0 Silent Honors Ark Knight',
    )


if __name__ == '__main__':
    root = Tk()

    gui = TKGui(root)
    gui.menuConfig()
    gui.infoStore()
    gui.infoLabel()
    gui.pingBox()

    root.mainloop()
