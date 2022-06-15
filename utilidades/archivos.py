import os
from tkinter import filedialog
import configuraciones.constantes as const


def normpath(url=str()):
    return os.path.expanduser(os.path.normpath(url))


def es_archivo(url=str()):
    if not os.path.isfile(os.path.expanduser(os.path.normpath(url))):
        return False
    return True


def file_browser(parent_window):
    ex_str = ''
    for ext in const.membrete_extensiones:
        ex_str += ext + ' '
    ex_str.rstrip(' ')
    tipos = [('Archivos de imagen', ex_str)]
    archivo_url = filedialog.askopenfilename(parent=parent_window, title='Seleccionar logo',
                                             filetypes=tipos)
    if str(archivo_url) == '()':
        return None
    return normpath(archivo_url)
