from tkinter import *
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter import messagebox as mBox
from tkinter import Menu

C = 12
H = 1
O = 16
N = 32
S = 17

def Funcion():
    selector = opcion1.get()
    if selector==1:
        entrada4.set('0')
        entrada5.set('0')
        entrada3.set('0')
    elif selector==2:
        entrada4.set('0')
        entrada5.set('0')
    elif selector==3:
        entrada5.set('0')
    else:
        print('CHONS')

def Mensaje():
    carbono=entrada1.get()
    higrogeno=entrada2.get()
    oxigeno=entrada3.get()
    nitrogeno=entrada4.get()
    azufre=entrada5.get()
    nombre_result=f'C{carbono} H{higrogeno} O{oxigeno} N{nitrogeno} S{azufre}'
    resultado:float=(carbono*C)+(higrogeno*H)+(oxigeno*O)+(nitrogeno*N)+(azufre*S)
    mBox.showinfo('Respuesta',f'La masa molar del [ {nombre_result} ] es {resultado} kg/kmol')


def Salir():
    root.destroy()
    root.quit()

root = Tk()
root.wm_title('Molar_Organic')
root.geometry('400x400')
root.resizable(0, 0)

imagen =PhotoImage(file='molar.png')
Label(root,image=imagen,bd=12).pack()
#------------------------------------------
barra_menu = Menu(root)
root.config(menu=barra_menu)

funcionamiento = Menu(barra_menu,tearoff=0)
funcionamiento.add_command(label = 'Funcionamiento')
funcionamiento.add_separator()
funcionamiento.add_command(label='Ayuda')
funcionamiento.add_separator()
funcionamiento.add_command(label='Referencias')
barra_menu.add_cascade(label = 'Acerca de: ',menu=funcionamiento)

#------------------------------------------
etiqueta = StringVar()
etiqueta = Label(root, text='Seleccione las sustancia quimica a calcular')
etiqueta.place(x=0,y=40)

opcion1 = IntVar()
radio1 = Radiobutton(root,text='Carbono-Hidrogeno',variable=opcion1,value=1, command=Funcion)
radio1.place(x=0,y=20+40)
radio2 = Radiobutton(root,text='Carbono-Hidrogeno-Oxigeno',variable=opcion1,value=2, command=Funcion)
radio2.place(x=0,y=40+40)
radio3 = Radiobutton(root,text='Carbono-Hidrogeno-Oxigeno-Nitrogeno',variable=opcion1,value=3, command=Funcion)
radio3.place(x=0,y=60+40)
radio4 = Radiobutton(root,text='Carbono-Hidrogeno-Oxigeno-Nitrogeno-Azufre',variable=opcion1,value=4, command=Funcion)
radio4.place(x=0,y=80+40)
#----------------------------------------
titulo1=StringVar()
titulo1=Label(root,text='Ingrese la cantidad de elementos:')
titulo1.place(x=0,y=120+40)

#----------------------------------------
etiqueta2 = StringVar()
etiqueta2 = Label(root,text='Carbono',justify=CENTER)
etiqueta2.place(x=0,y=150+40)
entrada1= IntVar()
entrada1.set('')
Cabro = Entry(root,textvariable=entrada1,justify=CENTER)
Cabro.place(x=0,y=175+40)
#----------------------------------------
etiqueta3 = StringVar()
etiqueta3 = Label(root,text='Hidogeno',justify=CENTER)
etiqueta3.place(x=0,y=200+40)
entrada2 =IntVar()
entrada2.set('')
Hidro = Entry(root,textvariable=entrada2,justify=CENTER)
Hidro.place(x=0,y=225+40)
#---------------------------------------
etiqueta4 = StringVar()
etiqueta4 = Label(root,text='Oxigeno',justify=CENTER)
etiqueta4.place(x=200,y=150+40)
entrada3 =IntVar()
entrada3.set('')
Oxi = Entry(root,textvariable=entrada3,justify=CENTER)
Oxi.place(x=200,y=175+40)
#--------------------------------------
etiqueta5 = StringVar()
etiqueta5 = Label(root,text='Nitrogeno',justify=CENTER)
etiqueta5.place(x=200,y=200+40)
entrada4 =IntVar()
entrada4.set('')
Nitro = Entry(root,textvariable=entrada4,justify=CENTER)
Nitro.place(x=200,y=225+40)
#-------------------------------------
etiqueta6 = StringVar()
etiqueta6 = Label(root,text='Azufre',justify=CENTER)
etiqueta6.place(x=0,y=250+40)
entrada5 =IntVar()
entrada5.set('')
Azuf = Entry(root,textvariable=entrada5,justify=CENTER)
Azuf.place(x=0,y=275+40)
#-------------------------------------
boton1 = Button(root,text='SALIR',command=Salir)
boton1.place(x=350,y=360)
#------------------------------------
boton2 = Button(root,text='Calcular',command=Mensaje)
boton2.place(x=250,y=360)

root.mainloop()
