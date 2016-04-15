from tkinter import *


def doNothing():
    print('to do')


root = Tk()

# Menu

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New File', command=doNothing)
submenu.add_command(label='Open File', command=doNothing)
submenu.add_command(label='Open Folder', command=doNothing)
submenu.add_separator()
submenu.add_command(label='Exit', command=doNothing)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Copy', command=doNothing)
editmenu.add_command(label='Cut', command=doNothing)
editmenu.add_command(label='Paste', command=doNothing)
editmenu.add_separator()
editmenu.add_command(label='Line', command=doNothing)
editmenu.add_command(label='Comment', command=doNothing)

# Toolbar

toolbar = Frame(root, bg='blue')
toolbar.pack(side=TOP, fill=X)
insertbutton = Button(toolbar, text='Insert Image', command=doNothing)
insertbutton.pack(side=LEFT, padx=2, pady=2)
printbutton = Button(toolbar, text='Print', command=doNothing)
printbutton.pack(side=LEFT, padx=2, pady=2)

# Statusbar

status = Label(root, text='Saving', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
