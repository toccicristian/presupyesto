import modelos.configuracion
import configuraciones.constantes as const
import json
import os
from utilidades.archivos import normpath


def lee_configuracion ():
    config=modelos.configuracion.Configuracion()
    if os.path.isfile(normpath(const.configuracion_url)):
        with open (normpath(const.configuracion_url), 'r') as ar_conf:
            config.__dict__=json.load(ar_conf)
    return config


def escribe_configuracion (conf = modelos.configuracion.Configuracion()):
    with open (normpath(const.configuracion_url), 'w') as ar_conf:
        json.dump(conf.__dict__, ar_conf)
