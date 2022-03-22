import tkinter
import tkinter as tk
import controladores.botones_basededatos
import controladores.barra_busqueda
import controladores.caja_resultados


def dibuja():
    # region definiciones
    framew = 0
    ventana_principal = tk.Tk()

    #   AREA PRESUPUESTO:
    marco_sup = tk.Frame(width='400', height='300')
    marco_lista_presup = tk.Frame(marco_sup)
    lista_presup = tk.Listbox(marco_lista_presup, width='150', height='20')
    scrollbar_lista_presup = tk.Scrollbar(marco_lista_presup)
    lista_presup.config(yscrollcommand=scrollbar_lista_presup.set)
    scrollbar_lista_presup.config(command=lista_presup.yview)
    boton_generar = tk.Button(marco_sup, text='GENERAR')

    #   AREA BD:
    marco_inf = tk.Frame(width='300', height='300')
    #   BD - BUSQUEDA:
    marco_inf_iz = tk.Frame(marco_inf, width='150', height='300', highlightbackground='black',
                            highlightthickness=framew)
    marco_inf_iz_titulo = tk.Frame(marco_inf_iz, highlightbackground='black', highlightthickness=framew)
    label_busqueda = tk.Label(marco_inf_iz_titulo, text='Búsqueda :')
    entry_busqueda = tk.Entry(marco_inf_iz, width='60')
    marco_inf_iz_res_busqueda = tk.Frame(marco_inf_iz, highlightbackground='black', highlightthickness=framew)
    res_busqueda = tk.Listbox(marco_inf_iz_res_busqueda, width='60')
    scrollb_res_busqueda = tk.Scrollbar(marco_inf_iz_res_busqueda, orient='vertical')
    res_busqueda.config(yscrollcommand=scrollb_res_busqueda.set)
    scrollb_res_busqueda.config(command=res_busqueda.yview)

    #   BD - DETALLES:
    marco_inf_der = tk.Frame(marco_inf, highlightbackground='black', highlightthickness=framew)
    marco_inf_der_titulo = tk.Frame(marco_inf_der, highlightbackground='black', highlightthickness=framew)
    marco_inf_der_contenidos = tk.Frame(marco_inf_der, highlightbackground='black', highlightthickness=framew)
    marco_inf_der_contenidos_coliz = tk.Frame(marco_inf_der_contenidos, highlightbackground='black',
                                              highlightthickness=framew)
    marco_inf_der_contenidos_colde = tk.Frame(marco_inf_der_contenidos, highlightbackground='black',
                                              highlightthickness=framew)
    label_detalles = tk.Label(marco_inf_der_titulo, text='DETALLES')
    label_tags = tk.Label(marco_inf_der_contenidos_coliz, text='Tags:')
    detalles_tags = tk.Entry(marco_inf_der_contenidos_colde, width='40')
    label_nombre = tk.Label(marco_inf_der_contenidos_coliz, text='Nombre:')
    detalles_nombre = tk.Entry(marco_inf_der_contenidos_colde, width='40')
    label_costo = tk.Label(marco_inf_der_contenidos_coliz, text='Costo:')
    detalles_costo = tk.Entry(marco_inf_der_contenidos_colde, width='40')
    label_t_cambio = tk.Label(marco_inf_der_contenidos_coliz, text='T.Cambio::')
    detalles_t_cambio = tk.Entry(marco_inf_der_contenidos_colde, width='40')
    label_descripcion = tk.Label(marco_inf_der_contenidos_coliz, text='Descripcion:')
    marco_inf_der_contenidos_colde_descr = tk.Frame(marco_inf_der_contenidos_colde, highlightbackground='black',
                                                    highlightthickness=framew)
    detalles_descripcion = tk.Text(marco_inf_der_contenidos_colde_descr, height='3', width='30')
    scrollb_detalles = tk.Scrollbar(marco_inf_der_contenidos_colde_descr)
    detalles_descripcion.config(yscrollcommand=scrollb_detalles.set)
    scrollb_detalles.config(command=detalles_descripcion.yview)
    label_existencias = tk.Label(marco_inf_der_contenidos_coliz, text='Existencias:')
    detalles_existencias = tk.Entry(marco_inf_der_contenidos_colde, width='40')
    label_url = tk.Label(marco_inf_der_contenidos_coliz, text='URL:')
    detalles_url = tk.Entry(marco_inf_der_contenidos_colde, width='40')
    #   BD - PLUGINS Y OPCIONES:
    marco_opciones = tk.Frame(marco_inf)
    auto_var=tkinter.IntVar()
    auto_checkbox = tk.Checkbutton(marco_opciones,text='Auto',variable=auto_var)
    #   BD Y PRESUPUESTO- AGREGAR Y QUITAR:
    marco_inf_cent = tk.Frame(marco_inf, highlightbackground='black', highlightthickness=framew)
    marco_inf_cent_titulo1 = tk.Frame(marco_inf_cent, highlightbackground='black', highlightthickness=framew)
    label_presupuestoagregaroquitar = tk.Label(marco_inf_cent_titulo1, text='Presupuesto')
    marco_inf_cent_botones1 = tk.Frame(marco_inf_cent, highlightbackground='black', highlightthickness=framew)
    boton_agregar_a_presupuesto = tk.Button(marco_inf_cent_botones1, width='5', height='2', text='+')
    boton_quitar_de_presupuesto = tk.Button(marco_inf_cent_botones1, width='5', height='2', text='-')
    marco_inf_cent_titulo2 = tk.Frame(marco_inf_cent, highlightbackground='black', highlightthickness=framew)
    label_basededatosagregaroquitar = tk.Label(marco_inf_cent_titulo2, text='Base de datos')
    marco_inf_cent_botones2 = tk.Frame(marco_inf_cent, highlightbackground='black', highlightthickness=framew)
    boton_agregar_a_base_de_datos = tk.Button(marco_inf_cent_botones2, width='5', height='2', text='+',
                                              command=lambda: controladores.botones_basededatos.agregar_producto(
                                                  detalles_tags,detalles_nombre,detalles_costo,detalles_t_cambio,
                                                  detalles_descripcion,detalles_existencias,detalles_url,auto_var
                                              ))
    boton_quitar_de_base_de_datos = tk.Button(marco_inf_cent_botones2, width='5', height='2', text='-')
    # endregion
    # region packing-superior
    marco_sup.pack(side='top', fill='x')
    marco_lista_presup.pack(side='left', padx=(10, 0), pady=(10, 10))
    lista_presup.pack(side='left', fill='both', padx='0', pady='10')
    scrollbar_lista_presup.pack(side='right', fill='both')
    boton_generar.pack(side='top', padx=(10, 10), pady=(10, 10))
    # endregion
    marco_inf.pack(side='top', fill='x')
    # region packing-inf-izq
    marco_inf_iz.pack(side='left', pady=('0', '10'))
    marco_inf_iz_titulo.pack(side='top', fill='x')
    label_busqueda.pack(side='left', padx='10', pady=('10', '0'))
    entry_busqueda.pack(side='top', padx='10', pady=('0', '5'))
    marco_inf_iz_res_busqueda.pack(side='top')
    res_busqueda.pack(side='left', padx=('10', '0'), pady=('5', '10'))
    scrollb_res_busqueda.pack(side='left', fill='both')
    # endregion
    # region packing-inf-cent
    marco_inf_cent.pack(side='left', padx=('40','40'),pady=('0', '20'))
    marco_inf_cent_titulo1.pack(side='top')
    label_presupuestoagregaroquitar.pack(side='left')
    marco_inf_cent_botones1.pack(side='top', pady=('0', '50'))
    boton_quitar_de_presupuesto.pack(side='left')
    boton_agregar_a_presupuesto.pack(side='left')
    marco_inf_cent_titulo2.pack(side='top', pady=('50', '0'))
    label_basededatosagregaroquitar.pack(side='left')
    marco_inf_cent_botones2.pack(side='top')
    boton_quitar_de_base_de_datos.pack(side='left')
    boton_agregar_a_base_de_datos.pack(side='left')
    # endregion
    # region packing-inf-der
    marco_inf_der.pack(side='left', fill='y', padx=('0','0'), pady=('0', '10'))
    marco_inf_der_titulo.pack(side='top')
    label_detalles.pack(side='top', pady=('10', '0'))
    marco_inf_der_contenidos.pack(side='top')
    marco_inf_der_contenidos_coliz.pack(side='left', pady=('0', '0'))
    label_tags.pack(side='top', anchor='w', padx='10')
    label_nombre.pack(side='top', anchor='w', padx='10')
    label_costo.pack(side='top', anchor='w', padx='10')
    label_t_cambio.pack(side='top', anchor='w', padx='10')
    label_descripcion.pack(side='top', anchor='w', padx='10', pady=('15', '10'))
    label_existencias.pack(side='top', anchor='w', padx='10')
    label_url.pack(side='top', anchor='w', padx='10')
    marco_inf_der_contenidos_colde.pack(side='left')
    detalles_tags.pack(side='top', padx='10')
    detalles_nombre.pack(side='top', padx='10')
    detalles_costo.pack(side='top', padx='10')
    detalles_t_cambio.pack(side='top', padx='10')
    marco_inf_der_contenidos_colde_descr.pack(side='top')
    detalles_descripcion.pack(side='left', padx=('15', '0'))
    scrollb_detalles.pack(side='left', fill='both')
    detalles_existencias.pack(side='top', padx='10')
    detalles_url.pack(side='top', padx='10')
    # endregion
    # region packing-opciones
    marco_opciones.pack(side='left',anchor='n',pady=('20','0'))
    auto_checkbox.pack(side='top')
    # endregion
    # region bindeos
    entry_busqueda.bind('<Return>',lambda x: controladores.barra_busqueda.busca(entry_busqueda,res_busqueda))
    res_busqueda.bind('<<ListboxSelect>>', lambda x: controladores.caja_resultados.presenta_producto(
        res_busqueda,detalles_tags,detalles_nombre,detalles_costo,detalles_t_cambio,detalles_descripcion,
        detalles_existencias,detalles_url,auto_var))
    # endregion
    ventana_principal.mainloop()
