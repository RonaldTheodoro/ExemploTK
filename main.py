from tkinter import *
from tkinter import messagebox


def todo():
    messagebox.showinfo('to do', 'to do')


class TkGui:

    def __init__(self, root):
        self.root = root
        # Titulo da janela principal
        self.root.title('Numeron Network')

        self.font = ("Verdana", "12")

        # Tamanho da janela principal
        self.root.geometry('640x600')

        # Frame contendo as informações
        self.info = Frame(self.root, width=600)
        # 'flat' 'raised' 'ridge' 'sunken' 'groove'
        self.info.pack(fill=X, padx=5, pady=5)

        # Dados das lojas
        # Codigo
        Label(self.info, text='Codigo: ', font=self.font).grid(
                row=0, column=0, padx=5, pady=5, sticky=W)
        self.code = Entry(self.info, width=2, font=self.font, relief='ridge')
        self.code.grid(row=0, column=1, sticky=W+E)

        # Nome da loja
        Label(self.info, text='Loja: ', font=self.font).grid(
                row=0, column=2, sticky=W)
        self.store = Label(self.info, text='', font=self.font)
        self.store['bg'] = 'white'
        self.store['relief'] = 'ridge'
        self.store.grid(row=0, column=3, columnspan=3, sticky=W+E)

        # Ramal
        Label(self.info, text='Ramal: ', font=self.font).grid(
                row=1, column=0, padx=5, pady=5, sticky=W)
        self.ramal = Label(self.info, text='', width=4, font=self.font)
        self.ramal['bg'] = 'white'
        self.ramal['relief'] = 'ridge'
        self.ramal.grid(row=1, column=1, sticky=W+E)

        # Telefone
        Label(self.info, text='Tel: ', font=self.font).grid(
                row=1, column=2, sticky=W)
        self.phone = Label(self.info, text='', width=15, font=self.font)
        self.phone['bg'] = 'white'
        self.phone['relief'] = 'ridge'
        self.phone.grid(row=1, column=3, sticky=W+E)

        # Grife
        Label(self.info, text='Grife: ', font=self.font).grid(
                row=1, column=4, sticky=W)
        self.grife = Label(self.info, text='', width=16, font=self.font)
        self.grife['bg'] = 'white'
        self.grife['relief'] = 'ridge'
        self.grife.grid(row=1, column=5, sticky=W+E)

        # Endereço
        Label(self.info, text='Endereço: ', font=self.font).grid(
                row=2, column=0, padx=5, pady=5, sticky=W)
        self.address = Label(self.info, text='', font=self.font)
        self.address['bg'] = 'white'
        self.address['relief'] = 'ridge'
        self.address.grid(row=2, column=1, columnspan=5, sticky=W+E)

        # Supervisor
        Label(self.info, text='Supervisor: ', font=self.font).grid(
                row=3, column=0, sticky=W)
        self.supervisor = Label(self.info, text='', width=15, font=self.font)
        self.supervisor['bg'] = 'white'
        self.supervisor['relief'] = 'ridge'
        self.supervisor.grid(row=3, column=1, columnspan=2, sticky=W+E)

        # CNPJ
        Label(self.info, text='CNPJ: ', font=self.font).grid(
                row=3, column=3, padx=5, pady=5, sticky=W)
        self.cnpj = Label(self.info, text='', font=self.font)
        self.cnpj['bg'] = 'white'
        self.cnpj['relief'] = 'ridge'
        self.cnpj.grid(row=3, column=4, columnspan=2, sticky=W+E)

        # Botão de busca
        self.btsearch = Button(self.info, text='Buscar loja', command=self.bt)
        self.btsearch['font'] = self.font
        self.btsearch['width'] = 60
        self.btsearch.grid(row=4, column=0, columnspan=6, pady=5, sticky=W+E)

        self.pingbox = Frame(self.root, width=530)
        self.pingbox.pack(fill=X)

        self.ip1 = Label(self.pingbox, text='Ip 01')
        self.ip1.grid(row=0, column=0)

    def bt(self):
        self.store['text'] = 'Av Paulista'
        self.ramal['text'] = '3081'
        self.phone['text'] = '1163636363'
        self.grife['text'] = 'Colombo'
        self.address['text'] = 'Av Paulista Nº 1380'
        self.supervisor['text'] = 'João Ferreira Neto'
        self.cnpj['text'] = '12345678912345'

root = Tk()

gui = TkGui(root)

root.mainloop()
