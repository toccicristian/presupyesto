import tkinter


def dibuja():
    #   #####################          DEFINICIONES Y SETTING:    ######################
    framew=0
    ventana_principal = tkinter.Tk()
    #   AREA PRESUPUESTO:
    marco_superior = tkinter.Frame(width='400', height='300')
    lista_presupuesto = tkinter.Listbox(marco_superior, width='150', height='20')

    #   AREA BD:
    marco_inf = tkinter.Frame(width='300', height='300')
    #   BD - BUSQUEDA:
    marco_infizq = tkinter.Frame(marco_inf, width='100', height='300', highlightbackground='black',
                                       highlightthickness=framew)
    marco_infizq_titulo = tkinter.Frame(marco_infizq, highlightbackground='black', highlightthickness=framew)
    label_busqueda = tkinter.Label(marco_infizq_titulo, text='Búsqueda :')
    entry_busqueda = tkinter.Entry(marco_infizq, width='40')
    marco_infizq_result_busqueda=tkinter.Frame(marco_infizq, highlightbackground='black', highlightthickness=framew)
    result_busqueda = tkinter.Listbox(marco_infizq_result_busqueda, width='40')
    scrollbar_result_busqueda=tkinter.Scrollbar(marco_infizq_result_busqueda,orient='vertical')
    #   contrato con scrollbar:
    result_busqueda.config(yscrollcommand=scrollbar_result_busqueda.set)
    scrollbar_result_busqueda.config(command=result_busqueda.yview)

    #   BD - DETALLES:
    marco_infcentr = tkinter.Frame(marco_inf, highlightbackground='black', highlightthickness=framew)
    marco_infcentr_titulo = tkinter.Frame(marco_infcentr, highlightbackground='black', highlightthickness=framew)
    marco_infcentr_contenidos = tkinter.Frame(marco_infcentr, highlightbackground='black', highlightthickness=framew)
    marco_infcentr_contenidos_coliz = tkinter.Frame(
        marco_infcentr_contenidos,highlightbackground='black', highlightthickness=framew)
    marco_infcentr_contenidos_colde = tkinter.Frame(
        marco_infcentr_contenidos, highlightbackground='black', highlightthickness=framew)
    label_detalles = tkinter.Label(marco_infcentr_titulo, text='DETALLES')
    label_tags = tkinter.Label(marco_infcentr_contenidos_coliz, text='Tags:')
    detalles_tags = tkinter.Entry(marco_infcentr_contenidos_colde, width='40')
    label_nombre = tkinter.Label(marco_infcentr_contenidos_coliz, text='Nombre:')
    detalles_nombre = tkinter.Entry(marco_infcentr_contenidos_colde, width='40')
    label_costo = tkinter.Label(marco_infcentr_contenidos_coliz, text='Costo:')
    detalles_costo = tkinter.Entry(marco_infcentr_contenidos_colde, width='40')
    label_t_cambio = tkinter.Label(marco_infcentr_contenidos_coliz, text='T.Cambio::')
    detalles_t_cambio = tkinter.Entry(marco_infcentr_contenidos_colde, width='40')
    label_descripcion = tkinter.Label(marco_infcentr_contenidos_coliz, text='Descripcion:')
    marco_infcentr_contenidos_colde_descripcion=tkinter.Frame(
        marco_infcentr_contenidos_colde,highlightbackground='black', highlightthickness=framew)
    detalles_descripcion = tkinter.Text(marco_infcentr_contenidos_colde_descripcion, height='3', width='30')
    scrollbar_detalles = tkinter.Scrollbar(marco_infcentr_contenidos_colde_descripcion)
    #   contrato con scrollbar:
    detalles_descripcion.config(yscrollcommand=scrollbar_detalles.set)
    scrollbar_detalles.config(command=detalles_descripcion.yview)

    label_existencias = tkinter.Label(marco_infcentr_contenidos_coliz, text='Existencias:')
    detalles_existencias = tkinter.Entry(marco_infcentr_contenidos_colde, width='40')
    label_url = tkinter.Label(marco_infcentr_contenidos_coliz, text='URL:')
    detalles_url = tkinter.Entry(marco_infcentr_contenidos_colde, width='40')
    #   BD Y PRESUPUESTO- AGREGAR Y QUITAR:
    marco_inferior_derecho = tkinter.Frame(marco_inf, highlightbackground='black', highlightthickness=framew)
    marco_inferior_derecho_titulo1 = tkinter.Frame(marco_inferior_derecho, highlightbackground='black',
                                                   highlightthickness=framew)
    label_presupuestoagregaroquitar = tkinter.Label(marco_inferior_derecho_titulo1, text='Presupuesto')
    marco_inferior_derecho_botones1 = tkinter.Frame(marco_inferior_derecho, highlightbackground='black',
                                                    highlightthickness=framew)
    boton_agregar_a_presupuesto = tkinter.Button(marco_inferior_derecho_botones1, width='5', height='2', text='+')
    boton_quitar_de_presupuesto = tkinter.Button(marco_inferior_derecho_botones1, width='5', height='2', text='-')
    marco_inferior_derecho_titulo2 = tkinter.Frame(marco_inferior_derecho, highlightbackground='black',
                                                   highlightthickness=framew)
    label_basededatosagregaroquitar = tkinter.Label(marco_inferior_derecho_titulo2, text='Base de datos')
    marco_inferior_derecho_botones2 = tkinter.Frame(marco_inferior_derecho, highlightbackground='black',
                                                    highlightthickness=framew)
    boton_agregar_a_base_de_datos = tkinter.Button(marco_inferior_derecho_botones2, width='5', height='2', text='+')
    boton_quitar_de_base_de_datos = tkinter.Button(marco_inferior_derecho_botones2, width='5', height='2', text='-')
    #   #####################          DIBUJADO DE LOS ELEMENTOS:    ######################
    marco_superior.pack(side='top', fill='x')
    lista_presupuesto.pack(side='left', padx='10', pady='10')
    marco_inf.pack(side='top', fill='x')
    marco_infizq.pack(side='left', pady=('0', '10'))
    marco_infizq_titulo.pack(side='top', fill='x')
    label_busqueda.pack(side='left', padx='10', pady=('10', '0'))
    entry_busqueda.pack(side='top', padx='10', pady=('0', '5'))
    marco_infizq_result_busqueda.pack(side='top')
    result_busqueda.pack(side='left', padx=('10','0'), pady=('5', '10'))
    scrollbar_result_busqueda.pack(side='left',fill='both')
    marco_infcentr.pack(side='left', fill='y', padx='60', pady=('0', '10'))
    marco_infcentr_titulo.pack(side='top')
    label_detalles.pack(side='top', pady=('10', '0'))
    marco_infcentr_contenidos.pack(side='top')
    marco_infcentr_contenidos_coliz.pack(side='left', pady=('0', '0'))
    label_tags.pack(side='top', anchor='w', padx='10')
    label_nombre.pack(side='top', anchor='w', padx='10')
    label_costo.pack(side='top', anchor='w', padx='10')
    label_t_cambio.pack(side='top', anchor='w', padx='10')
    label_descripcion.pack(side='top', anchor='w', padx='10', pady=('15', '10'))
    label_existencias.pack(side='top', anchor='w', padx='10')
    label_url.pack(side='top', anchor='w', padx='10')
    marco_infcentr_contenidos_colde.pack(side='left')
    detalles_tags.pack(side='top', padx='10')
    detalles_nombre.pack(side='top', padx='10')
    detalles_costo.pack(side='top', padx='10')
    detalles_t_cambio.pack(side='top', padx='10')
    marco_infcentr_contenidos_colde_descripcion.pack(side='top')
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

