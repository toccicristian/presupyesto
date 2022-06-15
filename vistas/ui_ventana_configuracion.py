import tkinter as tk
import controladores.v_config
import controladores.v_config_botones


def dibuja(v_principal):
    v_config = tk.Toplevel(v_principal)
    v_config_min_w = 500
    v_config_min_h = 200
    v_config.minsize(v_config_min_w, v_config_min_h)
    v_config.grab_set()

    v_config.title('Presupyesto - Configuración')
    f_membrete_altura = tk.Frame(v_config)
    l_membrete_altura = tk.Label(f_membrete_altura, text='Altura del logo (Px)        :')
    entry_membrete_altura = tk.Entry(f_membrete_altura, width='5')
    f_membrete_pos_x = tk.Frame(v_config)
    l_membrete_pos_x = tk.Label(f_membrete_pos_x, text='Posicion horiz. del logo  :')
    entry_membrete_pos_x = tk.Entry(f_membrete_pos_x, width='5')
    f_logo_url = tk.Frame(v_config)
    f_button_y_canvas_url = tk.Frame(f_logo_url)
    canvas_logo = tk.Canvas(f_button_y_canvas_url, width=256, height=256, bg='white')
    entry_logo_url = tk.Entry(f_logo_url, width=40)
    b_logo_url = tk.Button(f_button_y_canvas_url, text='Seleccionar logo...',
                           command=lambda: controladores.v_config_botones.examinar(
                               v_config, entry_logo_url, canvas_logo))
    f_info = tk.Frame(v_config)
    l_info = tk.Label(f_info, text='Info extra del membrete :')
    text_info = tk.Text(f_info, width=40, height=4)
    scrollbar_info = tk.Scrollbar(f_info, orient='vertical')
    text_info.config(yscrollcommand=scrollbar_info.set)
    scrollbar_info.config(command=text_info.yview)
    f_nota_al_pie = tk.Frame(v_config)
    l_nota_al_pie = tk.Label(f_nota_al_pie, text='Nota al pie del presup.   :')
    entry_nota_al_pie = tk.Entry(f_nota_al_pie, width='46')
    f_guardar_cancelar = tk.Frame(v_config)
    b_guardar = tk.Button(f_guardar_cancelar, text='Guardar',
                          command=lambda: controladores.v_config_botones.guarda_configuracion(
                              v_config,entry_membrete_altura, entry_membrete_pos_x, entry_logo_url,
                              text_info, entry_nota_al_pie))
    b_cancelar = tk.Button(f_guardar_cancelar, text='Cancelar', command=lambda: v_config.destroy())

    f_membrete_altura.pack(side=tk.TOP,anchor=tk.W, pady=(20, 5), padx=(15, 15))
    l_membrete_altura.pack(side=tk.LEFT)
    entry_membrete_altura.pack(side=tk.LEFT)
    f_membrete_pos_x.pack(side=tk.TOP,anchor=tk.W, pady=(5, 5), padx=(15, 15))
    l_membrete_pos_x.pack(side=tk.LEFT)
    entry_membrete_pos_x.pack(side=tk.LEFT)
    f_logo_url.pack(side=tk.TOP, anchor=tk.W, pady=(5, 5), padx=(15, 15))
    f_button_y_canvas_url.pack(side=tk.TOP, pady=(0,10))
    b_logo_url.pack(side=tk.LEFT)
    canvas_logo.pack(side=tk.LEFT, padx=(15,15))
    entry_logo_url.pack(side=tk.TOP)
    f_info.pack(side=tk.TOP,anchor=tk.W, pady=(5, 5), padx=(15, 15))
    l_info.pack(side=tk.LEFT)
    text_info.pack(side=tk.LEFT)
    scrollbar_info.pack(side=tk.LEFT, fill=tk.BOTH)
    f_nota_al_pie.pack(side=tk.TOP,anchor=tk.W, pady=(5, 5), padx=(15, 15))
    l_nota_al_pie.pack(side=tk.LEFT)
    entry_nota_al_pie.pack(side=tk.LEFT)
    f_guardar_cancelar.pack(side=tk.BOTTOM,anchor=tk.E, pady=(5, 20), padx=(15, 15))
    b_guardar.pack(side=tk.RIGHT, padx=(5, 0))
    b_cancelar.pack(side=tk.RIGHT, padx=(0, 5))

    controladores.v_config.muestra_configuracion(v_config,
                                                 entry_membrete_altura,
                                                 entry_membrete_pos_x,
                                                 canvas_logo,
                                                 entry_logo_url,
                                                 text_info,
                                                 entry_nota_al_pie)

    entry_membrete_altura.focus()
    v_config.mainloop()
