import tkinter
from tkinter import *

def mostrar ():
    ancho='800'
    alto='480'
    offsetx='10'
    offsety='20'
    ventana_principal = Tk()
    ventana_principal.title('PRESUPYESTO')
    ventana_principal.geometry(ancho+'x'+alto+'+'+offsetx+'+'+offsety)

    listbox_presupuesto = tkinter.Listbox(width=95, height=15)
    listbox_db = tkinter.Listbox(width=40,height=8)
    entry_busqueda_db = tkinter.Entry(width=40)
    boton_generar_presupuesto = tkinter.Button(text='GENERAR')
    boton_agregar_a_presupuesto = tkinter.Button(text='Agregar ^')
    boton_quitar_de_presupuesto = tkinter.Button(text='Quitar v')
    boton_agregar_a_bd = tkinter.Button(text='Agregar a BD ->')
    label_codigo = tkinter.Label(text='Codigo :')
    label_tags = tkinter.Label(text='Tags :')
    label_nombre = tkinter.Label(text='Nombre :')
    label_costo = tkinter.Label(text='Costo :')
    label_url = tkinter.Label(text='URL :')
    label_imagen_del_producto = tkinter.Label(text='imagen')
    text_codigo= tkinter.Text(state='disabled',height='1',width='20')
    text_tags=tkinter.Text(height='2',width='20',bg='white')
    text_nombre=tkinter.Text(height='1',width='20',bg='white')
    text_costo=tkinter.Text(height='1',width='20',bg='white')
    text_url=tkinter.Text(height='1',width='20',bg='white')

    boton_generar_presupuesto.place(x=int(ancho)-105,y=5)
    boton_agregar_a_presupuesto.place(x=250,y=int(int(alto)/2)+30)
    boton_quitar_de_presupuesto.place(x=350, y=int(int(alto)/2)+30)
    boton_agregar_a_bd.place(x=250,y=int(int(alto)/2)+164)
    listbox_presupuesto.place(x=5, y=5)
    entry_busqueda_db.place(x=440,y=int(int(alto)/2)+30)
    listbox_db.place(x=440,y=int(int(alto)/2)+60)
    label_codigo.place(x=5,y=int(int(alto)/2)+30)
    label_tags.place(x=5,y=int(int(alto)/2)+60)
    label_nombre.place(x=5,y=int(int(alto)/2)+110)
    label_costo.place(x=5,y=int(int(alto)/2)+140)
    label_url.place(x=5,y=int(int(alto)/2)+170)
    label_imagen_del_producto.place(x=255,y=int(int(alto)/2)+60)
    text_codigo.place(x=75,y=int(int(alto)/2)+30)
    text_tags.place(x=75,y=int(int(alto)/2)+60)
    text_nombre.place(x=75,y=int(int(alto)/2)+110)
    text_costo.place(x=75,y=int(int(alto)/2)+140)
    text_url.place(x=75,y=int(int(alto)/2)+170)

    ventana_principal.mainloop()
