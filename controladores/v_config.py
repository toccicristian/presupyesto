import repositorios.configuracion as conf
import tkinter as tk
import vistas.ui_ventana_configuracion
import configuraciones.constantes as const
import os


def muestra_configuracion(v_config,
                          entry_membrete_altura,
                          entry_membrete_pos_x,
                          canvas_logo,
                          entry_logo_url,
                          text_info,
                          entry_nota_al_pie):
    entry_membrete_altura.delete(0, tk.END)
    entry_membrete_altura.insert(tk.END, conf.lee_configuracion().get_membrete_altura())
    entry_membrete_pos_x.delete(0, tk.END)
    entry_membrete_pos_x.insert(tk.END, conf.lee_configuracion().get_membrete_pos_x())
    if os.path.isfile(os.path.expanduser(os.path.normpath(conf.lee_configuracion().get_membrete_url()))):
        imagen = tk.PhotoImage(file=conf.lee_configuracion().get_membrete_url())
        v_config.imagen=imagen
        canvas_logo.create_image(const.config_logo_preview_size[0],
                                 const.config_logo_preview_size[1],
                                 anchor=tk.NW,
                                 image=imagen)
    entry_logo_url.delete(0, tk.END)
    entry_logo_url.insert(tk.END, conf.lee_configuracion().get_membrete_url())
    text_info.delete('1.0', tk.END)
    text_info.insert('1.0', conf.lee_configuracion().get_info_as_string())
    entry_nota_al_pie.delete(0, tk.END)
    entry_nota_al_pie.insert(tk.END, conf.lee_configuracion().get_nota_al_pie())


def muesta_ventana(v_principal):
    vistas.ui_ventana_configuracion.dibuja(v_principal)