from tkinter import *
from tkinter import messagebox


root = Tk()


answer = messagebox.askquestion('Question 1', 'yes or no')

if answer == 'yes':
    messagebox.showinfo('teste', 'yes')
else:
    messagebox.showinfo('teste', 'no')

root.mainloop()
