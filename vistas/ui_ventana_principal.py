import tkinter
from tkinter import ttk
import tkinter as tk
import controladores.botones_basededatos
import controladores.barra_busqueda
import controladores.caja_resultados


def dibuja():
    # region definiciones
    framew = 0
    ventana_principal_minwidth = 1200
    ventana_principal = tk.Tk()
    ventana_principal.minsize(ventana_principal_minwidth, 680)

    marco_inf = tk.Frame(width='300', height='300')
    marco_inf_cent = tk.Frame(marco_inf, highlightbackground='black', highlightthickness=framew)
    label_barra_de_estado = tk.Label(bg='#000fff000', text='- ESTADO -', width='165')

    #   AREA PRESUPUESTO:
    marco_sup = tk.Frame(width='400', height='300')
    marco_lista_presup = tk.Frame(marco_sup)
    tview_presup = ttk.Treeview(marco_lista_presup, height=17, column=('c1', 'c2'), show='headings')
    tview_presup.column('# 1', anchor=tk.W, stretch=tk.YES, width='900')
    tview_presup.heading('# 1', text='Producto')
    tview_presup.column('# 2', anchor=tk.W, stretch=tk.YES, width='200')
    tview_presup.heading('#2', text='Costo')
    scrollb_presup = tk.Scrollbar(marco_lista_presup, orient='vertical')
    tview_presup.config(yscrollcommand=scrollb_presup.set)
    scrollb_presup.config(command=tview_presup.yview)

    boton_generar = tk.Button(marco_sup, text='GENERAR')

    #   AREA BD:
    #   BD - BUSQUEDA:
    marco_inf_iz = tk.Frame(marco_inf, width='150', height='300', highlightbackground='black',
                            highlightthickness=framew)
    marco_inf_iz_titulo = tk.Frame(marco_inf_iz, highlightbackground='black', highlightthickness=framew)
    label_busqueda = tk.Label(marco_inf_iz_titulo, text='Búsqueda :')
    entry_busqueda = tk.Entry(marco_inf_iz, width='60')
    marco_inf_iz_res_busqueda = tk.Frame(marco_inf_iz, highlightbackground='black', highlightthickness=framew)
    tview_res_busqueda = ttk.Treeview(marco_inf_iz_res_busqueda,height=6)
    tview_res_busqueda['columns'] = ('Item', 'Costo')
    tview_res_busqueda.column('#0', width=0, stretch=tk.NO)
    tview_res_busqueda.column('Item', anchor=tk.W, stretch=tk.YES, width='270')
    tview_res_busqueda.column('Costo', anchor=tk.W, stretch=tk.YES, width='150')
    tview_res_busqueda.heading('#0', text='', anchor=tk.W)
    tview_res_busqueda.heading('Item', text='Item', anchor=tk.W)
    tview_res_busqueda.heading('Costo', text='Costo', anchor=tk.W)
    scrollb_tview_res_busqueda = tk.Scrollbar(marco_inf_iz_res_busqueda, orient='vertical')
    tview_res_busqueda.config(yscrollcommand=scrollb_tview_res_busqueda.set)
    scrollb_tview_res_busqueda.config(command=tview_res_busqueda.yview)

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
    auto_var = tkinter.IntVar()
    auto_checkbox = tk.Checkbutton(marco_opciones, text='Auto', variable=auto_var)
    #   BD Y PRESUPUESTO- AGREGAR Y QUITAR:
    marco_inf_cent_titulo1 = tk.Frame(marco_inf_cent, highlightbackground='black', highlightthickness=framew)
    label_presupuestoagregaroquitar = tk.Label(marco_inf_cent_titulo1, text='Presupuesto')
    marco_inf_cent_botones1 = tk.Frame(marco_inf_cent, highlightbackground='black', highlightthickness=framew)
    boton_agregar_a_presupuesto = tk.Button(marco_inf_cent_botones1, width='5', height='2', text='+')
    boton_quitar_de_presupuesto = tk.Button(marco_inf_cent_botones1, width='5', height='2', text='-')
    marco_inf_cent_titulo2 = tk.Frame(marco_inf_cent, highlightbackground='black', highlightthickness=framew)
    label_basededatosagregaroquitar = tk.Label(marco_inf_cent_titulo2, text='Base de datos')
    marco_inf_cent_botones2 = tk.Frame(marco_inf_cent, highlightbackground='black', highlightthickness=framew)
    boton_agregar_a_base_de_datos = tk.Button(marco_inf_cent_botones2, width='3', height='2', text='+',
                                              command=lambda: controladores.botones_basededatos.agregar_producto_tview(
                                                  label_barra_de_estado, detalles_tags, detalles_nombre, detalles_costo,
                                                  detalles_t_cambio, detalles_descripcion, detalles_existencias,
                                                  detalles_url, auto_var, tview_res_busqueda
                                              ))
    boton_quitar_de_base_de_datos = tk.Button(marco_inf_cent_botones2, width='3', height='2', text='-',
                                              command=lambda: controladores.botones_basededatos.quitar_producto_tview(
                                                  label_barra_de_estado, tview_res_busqueda
                                              ))
    boton_modificar_de_base_de_datos = tk.Button(marco_inf_cent_botones2, width='3', height='2', text='<',
                                                 command=lambda: controladores.botones_basededatos.modificar_producto_tview(
                                                     label_barra_de_estado, tview_res_busqueda, detalles_tags,
                                                     detalles_nombre,
                                                     detalles_costo, detalles_t_cambio, detalles_descripcion,
                                                     detalles_existencias, detalles_url, auto_var
                                                 ))

    boton_barrer_borrados = tk.Button(marco_inf_cent, width='15', height='1', text='barrer borrados...',
                                      command=lambda: controladores.botones_basededatos.barrer_borrados(
                                          label_barra_de_estado))
    # endregion
    # region packing-superior
    marco_sup.pack(side='top', fill='x')
    marco_lista_presup.pack(side='left', padx=(10, 0), pady=(10, 10))
    tview_presup.pack(side='left', fill='both', padx='0', pady=('0', '0'))
    scrollb_presup.pack(side='right', fill='both')
    boton_generar.pack(side='top', padx=(10, 10), pady=(25, 10))
    # endregion
    marco_inf.pack(side='top', fill='x')
    # region packing-inf-izq
    marco_inf_iz.pack(side='left', pady=('0', '10'))
    marco_inf_iz_titulo.pack(side='top', fill='x')
    label_busqueda.pack(side='left', padx='10', pady=('10', '0'))
    entry_busqueda.pack(side='top', padx='10', pady=('0', '5'))
    marco_inf_iz_res_busqueda.pack(side='top')
    tview_res_busqueda.pack(side='left', padx=('10', '0'), pady=('5', '10'))
    scrollb_tview_res_busqueda.pack(side='left', fill='both')
    # endregion
    # region packing-inf-cent
    marco_inf_cent.pack(side='left', padx=('40', '40'), pady=('0', '20'))
    marco_inf_cent_titulo1.pack(side='top')
    label_presupuestoagregaroquitar.pack(side='left')
    marco_inf_cent_botones1.pack(side='top', pady=('0', '20'))
    boton_quitar_de_presupuesto.pack(side='left')
    boton_agregar_a_presupuesto.pack(side='left')
    marco_inf_cent_titulo2.pack(side='top', pady=('20', '0'))
    label_basededatosagregaroquitar.pack(side='left')
    marco_inf_cent_botones2.pack(side='top')
    boton_quitar_de_base_de_datos.pack(side='left')
    boton_modificar_de_base_de_datos.pack(side='left')
    boton_agregar_a_base_de_datos.pack(side='left')
    boton_barrer_borrados.pack(side='top', pady=('20', '0'))
    # endregion
    # region packing-inf-der
    marco_inf_der.pack(side='left', fill='y', padx=('0', '0'), pady=('0', '10'))
    marco_inf_der_titulo.pack(side='top')
    label_detalles.pack(side='top', pady=('10', '0'))
    marco_inf_der_contenidos.pack(side='top')
    marco_inf_der_contenidos_coliz.pack(side='left', pady=('0', '0'))
    label_tags.pack(side='top', anchor='w', padx='10')
    label_nombre.pack(side='top', anchor='w', padx='10')
    label_costo.pack(side='top', anchor='w', padx='10')
    label_t_cambio.pack(side='top', anchor='w', padx='10')
    label_descripcion.pack(side='top', anchor='w', padx='10', pady=('15', '10'))
    label_existencias.pack(side='top', anchor='w', padx='10', pady=('12', '0'))
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
    marco_opciones.pack(side='left', anchor='n', pady=('20', '0'))
    auto_checkbox.pack(side='top')
    # endregion
    label_barra_de_estado.pack(side='top', pady=('5', '0'))
    # region bindeos
    entry_busqueda.bind('<Return>',
                        lambda x: controladores.barra_busqueda.busca_tview(entry_busqueda, tview_res_busqueda))
    tview_res_busqueda.bind('<<TreeviewSelect>>', lambda x: controladores.caja_resultados.presenta_producto_tview(
        tview_res_busqueda, detalles_tags, detalles_nombre, detalles_costo, detalles_t_cambio, detalles_descripcion,
        detalles_existencias, detalles_url, auto_var))
    # endregion
    ventana_principal.mainloop()

# TODO : agregar crear funciones de agregar a presupuesto y agregar esas funciones a los botones
# TODO : agregar funcion de generar presupuesto y agregar esa funcion al boton generar
# TODO : IMPLEMENTAR SISTEMA DE PLUGINS
# TODO : (rediseño mayor, plan lejano) CREAR VENTANA ADMINISTRAR BD
