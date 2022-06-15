import modelos.configuracion
import repositorios.configuracion as conf
import configuraciones.constantes as const
import tkinter as tk
import utilidades.archivos
from utilidades.archivos import es_archivo


def guarda_configuracion(v_config,
                         entry_membrete_altura,
                         entry_membrete_pos_x,
                         entry_logo_url,
                         text_info,
                         entry_nota_al_pie):
    config = modelos.configuracion.Configuracion()
    config.set_membrete_altura(int(entry_membrete_altura.get()))
    config.set_membrete_pos_x(int(entry_membrete_pos_x.get()))
    config.set_membrete_url(entry_logo_url.get())
    config.set_info_as_string(text_info.get('1.0', 'end-1c'))
    config.set_nota_al_pie(entry_nota_al_pie.get())
    conf.escribe_configuracion(config)
    v_config.destroy()


def examinar(parent_window, entry_logo_url, canvas_logo):
    url = utilidades.archivos.file_browser(parent_window)
    if url is None or url == '' or not es_archivo(url):
        return False
    imagen = tk.PhotoImage(file=url)
    parent_window.imagen = imagen
    canvas_logo.create_image(const.config_logo_preview_size[0],
                             const.config_logo_preview_size[1],
                             anchor=tk.NW,
                             image=imagen)
    entry_logo_url.delete(0, tk.END)
    entry_logo_url.insert(tk.END, url)
