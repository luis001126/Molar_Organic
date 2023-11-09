from tkinter import *
import tkinter as ttk

root = Tk()
root.wm_title('Molar_Organic')
root.geometry('400x400')
root.resizable(0, 0)

etiquette = StringVar()
etiquette = Label(root, text='hola')
etiquette.pack()

root.mainloop()
