import tkinter


def dibuja():
    #   #####################          DEFINICIONES Y SETTING:    ######################
    grosor_de_marcos=0
    ventana_principal = tkinter.Tk()
    #   AREA PRESUPUESTO:
    marco_superior = tkinter.Frame(width='400', height='300')
    lista_presupuesto = tkinter.Listbox(marco_superior, width='150', height='20')

    #   AREA BD:
    marco_inferior = tkinter.Frame(width='300', height='300')
    #   BD - BUSQUEDA:
    marco_inferior_izq = tkinter.Frame(marco_inferior, width='100', height='300', highlightbackground='black',
                                       highlightthickness=grosor_de_marcos)
    marco_inferior_izq_titulo = tkinter.Frame(marco_inferior_izq, highlightbackground='black', highlightthickness=grosor_de_marcos)
    label_busqueda = tkinter.Label(marco_inferior_izq_titulo, text='Búsqueda :')
    entrada_busqueda = tkinter.Entry(marco_inferior_izq, width='40')
    marco_inferior_izq_resultados_busqueda=tkinter.Frame(marco_inferior_izq, highlightbackground='black', highlightthickness=grosor_de_marcos)
    resultados_busqueda = tkinter.Listbox(marco_inferior_izq_resultados_busqueda, width='40')
    scrollbar_resultados_busqueda=tkinter.Scrollbar(marco_inferior_izq_resultados_busqueda,orient='vertical')
    #   contrato con scrollbar:
    resultados_busqueda.config(yscrollcommand=scrollbar_resultados_busqueda.set)
    scrollbar_resultados_busqueda.config(command=resultados_busqueda.yview)

    #   BD - DETALLES:
    marco_inferior_central = tkinter.Frame(marco_inferior, highlightbackground='black', highlightthickness=grosor_de_marcos)
    marco_inferior_central_titulo = tkinter.Frame(marco_inferior_central, highlightbackground='black',
                                                  highlightthickness=grosor_de_marcos)
    marco_inferior_central_contenidos = tkinter.Frame(marco_inferior_central, highlightbackground='black',
                                                      highlightthickness=grosor_de_marcos)
    marco_inferior_central_contenidos_colizq = tkinter.Frame(marco_inferior_central_contenidos,
                                                             highlightbackground='black', highlightthickness=grosor_de_marcos)
    marco_inferior_central_contenidos_colder = tkinter.Frame(marco_inferior_central_contenidos,
                                                             highlightbackground='black', highlightthickness=grosor_de_marcos)
    label_detalles = tkinter.Label(marco_inferior_central_titulo, text='DETALLES')
    label_tags = tkinter.Label(marco_inferior_central_contenidos_colizq, text='Tags:')
    detalles_tags = tkinter.Entry(marco_inferior_central_contenidos_colder, width='40')
    label_nombre = tkinter.Label(marco_inferior_central_contenidos_colizq, text='Nombre:')
    detalles_nombre = tkinter.Entry(marco_inferior_central_contenidos_colder, width='40')
    label_costo = tkinter.Label(marco_inferior_central_contenidos_colizq, text='Costo:')
    detalles_costo = tkinter.Entry(marco_inferior_central_contenidos_colder, width='40')
    label_tipo_de_cambio = tkinter.Label(marco_inferior_central_contenidos_colizq, text='T.Cambio::')
    detalles_tipo_de_cambio = tkinter.Entry(marco_inferior_central_contenidos_colder, width='40')
    label_descripcion = tkinter.Label(marco_inferior_central_contenidos_colizq, text='Descripcion:')
    marco_inferior_central_contenidos_colder_descripcion=tkinter.Frame(marco_inferior_central_contenidos_colder,highlightbackground='black', highlightthickness=grosor_de_marcos)
    detalles_descripcion = tkinter.Text(marco_inferior_central_contenidos_colder_descripcion, height='3', width='30')
    scrollbar_detalles = tkinter.Scrollbar(marco_inferior_central_contenidos_colder_descripcion)
    #   contrato con scrollbar:
    detalles_descripcion.config(yscrollcommand=scrollbar_detalles.set)
    scrollbar_detalles.config(command=detalles_descripcion.yview)

    label_existencias = tkinter.Label(marco_inferior_central_contenidos_colizq, text='Existencias:')
    detalles_existencias = tkinter.Entry(marco_inferior_central_contenidos_colder, width='40')
    label_url = tkinter.Label(marco_inferior_central_contenidos_colizq, text='URL:')
    detalles_url = tkinter.Entry(marco_inferior_central_contenidos_colder, width='40')
    #   BD Y PRESUPUESTO- AGREGAR Y QUITAR:
    marco_inferior_derecho = tkinter.Frame(marco_inferior, highlightbackground='black', highlightthickness=grosor_de_marcos)
    marco_inferior_derecho_titulo1 = tkinter.Frame(marco_inferior_derecho, highlightbackground='black',
                                                   highlightthickness=grosor_de_marcos)
    label_presupuestoagregaroquitar = tkinter.Label(marco_inferior_derecho_titulo1, text='Presupuesto')
    marco_inferior_derecho_botones1 = tkinter.Frame(marco_inferior_derecho, highlightbackground='black',
                                                    highlightthickness=grosor_de_marcos)
    boton_agregar_a_presupuesto = tkinter.Button(marco_inferior_derecho_botones1, width='5', height='2', text='+')
    boton_quitar_de_presupuesto = tkinter.Button(marco_inferior_derecho_botones1, width='5', height='2', text='-')
    marco_inferior_derecho_titulo2 = tkinter.Frame(marco_inferior_derecho, highlightbackground='black',
                                                   highlightthickness=grosor_de_marcos)
    label_basededatosagregaroquitar = tkinter.Label(marco_inferior_derecho_titulo2, text='Base de datos')
    marco_inferior_derecho_botones2 = tkinter.Frame(marco_inferior_derecho, highlightbackground='black',
                                                    highlightthickness=grosor_de_marcos)
    boton_agregar_a_base_de_datos = tkinter.Button(marco_inferior_derecho_botones2, width='5', height='2', text='+')
    boton_quitar_de_base_de_datos = tkinter.Button(marco_inferior_derecho_botones2, width='5', height='2', text='-')
    #   #####################          DIBUJADO DE LOS ELEMENTOS:    ######################
    marco_superior.pack(side='top', fill='x')
    lista_presupuesto.pack(side='left', padx='10', pady='10')
    marco_inferior.pack(side='top', fill='x')
    marco_inferior_izq.pack(side='left', pady=('0', '10'))
    marco_inferior_izq_titulo.pack(side='top', fill='x')
    label_busqueda.pack(side='left', padx='10', pady=('10', '0'))
    entrada_busqueda.pack(side='top', padx='10', pady=('0', '5'))
    marco_inferior_izq_resultados_busqueda.pack(side='top')
    resultados_busqueda.pack(side='left', padx=('10','0'), pady=('5', '10'))
    scrollbar_resultados_busqueda.pack(side='left',fill='both')
    marco_inferior_central.pack(side='left', fill='y', padx='60', pady=('0', '10'))
    marco_inferior_central_titulo.pack(side='top')
    label_detalles.pack(side='top', pady=('10', '0'))
    marco_inferior_central_contenidos.pack(side='top')
    marco_inferior_central_contenidos_colizq.pack(side='left', pady=('0', '0'))
    label_tags.pack(side='top', anchor='w', padx='10')
    label_nombre.pack(side='top', anchor='w', padx='10')
    label_costo.pack(side='top', anchor='w', padx='10')
    label_tipo_de_cambio.pack(side='top', anchor='w', padx='10')
    label_descripcion.pack(side='top', anchor='w', padx='10', pady=('15', '10'))
    label_existencias.pack(side='top', anchor='w', padx='10')
    label_url.pack(side='top', anchor='w', padx='10')
    marco_inferior_central_contenidos_colder.pack(side='left')
    detalles_tags.pack(side='top', padx='10')
    detalles_nombre.pack(side='top', padx='10')
    detalles_costo.pack(side='top', padx='10')
    detalles_tipo_de_cambio.pack(side='top', padx='10')
    marco_inferior_central_contenidos_colder_descripcion.pack(side='top')
    detalles_descripcion.pack(side='left', padx=('15','0'))
    scrollbar_detalles.pack(side='left',fill='both')
    detalles_existencias.pack(side='top', padx='10')
    detalles_url.pack(side='top', padx='10')
    marco_inferior_derecho.pack(side='left',pady=('0','20'))
    marco_inferior_derecho_titulo1.pack(side='top')
    label_presupuestoagregaroquitar.pack(side='left')
    marco_inferior_derecho_botones1.pack(side='top', pady=('0', '50'))
    boton_quitar_de_presupuesto.pack(side='left')
    boton_agregar_a_presupuesto.pack(side='left')
    marco_inferior_derecho_titulo2.pack(side='top', pady=('50', '0'))
    label_basededatosagregaroquitar.pack(side='left')
    marco_inferior_derecho_botones2.pack(side='top')
    boton_quitar_de_base_de_datos.pack(side='left')
    boton_agregar_a_base_de_datos.pack(side='left')

    ventana_principal.mainloop()

