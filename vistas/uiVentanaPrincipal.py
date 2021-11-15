import tkinter

def dibuja():
    ventana_principal=tkinter.Tk()

    marco_superior=tkinter.Frame(width='300',height='300')
    lista_presupuesto=tkinter.Listbox(marco_superior,width='100',height='20')

    marco_inferior=tkinter.Frame(width='300',height='300')
    marco_inferior_izq1=tkinter.Frame(marco_inferior,width='100',height='300')
    label_busqueda=tkinter.Label(marco_inferior_izq1,text='Búsqueda :')
    entrada_busqueda=tkinter.Entry(marco_inferior_izq1,width='40')
    resultados_busqueda=tkinter.Listbox(marco_inferior_izq1,width='40')
    marco_inferior_central=tkinter.Frame(marco_inferior,highlightbackground='black',highlightthickness=1)
    marco_inferior_central_titulo=tkinter.Frame(marco_inferior_central,highlightbackground='black',highlightthickness=1)
    marco_inferior_central_contenidos=tkinter.Frame(marco_inferior_central,highlightbackground='black',highlightthickness=1)
    marco_inferior_central_contenidos_colizq=tkinter.Frame(marco_inferior_central_contenidos,highlightbackground='black',highlightthickness=1)
    marco_inferior_central_contenidos_colder=tkinter.Frame(marco_inferior_central_contenidos,highlightbackground='black',highlightthickness=1)
    label_detalles=tkinter.Label(marco_inferior_central_titulo,text='DETALLES')
    label_tags=tkinter.Label(marco_inferior_central_contenidos_colizq,text='Tags:')
    detalles_tags=tkinter.Entry(marco_inferior_central_contenidos_colder,width='40')
    label_nombre = tkinter.Label(marco_inferior_central_contenidos_colizq, text='Nombre:')
    detalles_nombre = tkinter.Entry(marco_inferior_central_contenidos_colder, width='40')
    label_costo = tkinter.Label(marco_inferior_central_contenidos_colizq, text='Costo:')
    detalles_costo = tkinter.Entry(marco_inferior_central_contenidos_colder, width='40')
    label_tipo_de_cambio = tkinter.Label(marco_inferior_central_contenidos_colizq, text='T.Cambio::')
    detalles_tipo_de_cambio = tkinter.Entry(marco_inferior_central_contenidos_colder, width='40')
    label_descripcion = tkinter.Label(marco_inferior_central_contenidos_colizq, text='Descripcion:')
    detalles_descripcion = tkinter.Text(marco_inferior_central_contenidos_colder, height='3',width='30')
    label_existencias = tkinter.Label(marco_inferior_central_contenidos_colizq, text='Existencias:')
    detalles_existencias = tkinter.Entry(marco_inferior_central_contenidos_colder, width='40')
    label_url=tkinter.Label(marco_inferior_central_contenidos_colizq,text='URL:')
    detalles_url=tkinter.Entry(marco_inferior_central_contenidos_colder,width='40')

    marco_superior.pack(side='top',fill='x')
    lista_presupuesto.pack(side='left',padx='10',pady='10')
    marco_inferior.pack(side='top',fill='x')
    marco_inferior_izq1.pack(side='left',pady=('0','10'))
    label_busqueda.pack(side='top',anchor='w',padx='10',pady=('10','0'))
    entrada_busqueda.pack(side='top',padx='10',pady=('0','5'))
    resultados_busqueda.pack(side='top',padx='10',pady=('5','10'))
    marco_inferior_central.pack(side='left',fill='y',pady=('0','10'))
    marco_inferior_central_titulo.pack(side='top')
    label_detalles.pack(side='top', pady=('10', '0'))
    marco_inferior_central_contenidos.pack(side='top')
    marco_inferior_central_contenidos_colizq.pack(side='left',pady=('0','0'))
    label_tags.pack(side='top', anchor='w', padx='10')
    label_nombre.pack(side='top', anchor='w', padx='10')
    label_costo.pack(side='top', anchor='w', padx='10')
    label_tipo_de_cambio.pack(side='top', anchor='w', padx='10')
    label_descripcion.pack(side='top', anchor='w', padx='10',pady=('15','10'))
    label_existencias.pack(side='top', anchor='w', padx='10')
    label_url.pack(side='top', anchor='w', padx='10')
    marco_inferior_central_contenidos_colder.pack(side='left')
    detalles_tags.pack(side='top',padx='10')
    detalles_nombre.pack(side='top',padx='10')
    detalles_costo.pack(side='top',padx='10')
    detalles_tipo_de_cambio.pack(side='top',padx='10')
    detalles_descripcion.pack(side='top',padx='10')
    detalles_existencias.pack(side='top',padx='10')
    detalles_url.pack(side='top',padx='10')

    ventana_principal.mainloop()

