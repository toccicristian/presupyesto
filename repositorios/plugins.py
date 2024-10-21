#!/usr/bin/python3

import os
import importlib
import modelos.modulo

# imports requeridos por algunos futuros plugins:
import requests
from bs4 import BeautifulSoup as bs
import modelos.producto


def lista_modulos(mod_dir):
    if not os.path.isdir(os.path.expanduser(os.path.normpath(mod_dir))):
        return False
    modulos = list()
    for f in os.listdir(os.path.expanduser(os.path.normpath(mod_dir))):
        if not f.startswith('__') and not f.endswith('.pyc'):
            modulos.append(modelos.modulo.Modulo(os.path.join(mod_dir, f)))
    return modulos


def importar(mod_dir):
    if not os.path.isdir(os.path.expanduser(os.path.normpath(mod_dir))):
        return False
    lista_plugins_importados = list()
    for f in os.listdir(os.path.expanduser(os.path.normpath(mod_dir))):
        if not f.startswith('__') and not f.endswith('.pyc'):
            modulo = modelos.modulo.Modulo(os.path.join(mod_dir, f))
            lista_plugins_importados.append(
                importlib.import_module(modulo.get_importable(), package=modulo.get_paquete()))
    return lista_plugins_importados


def test_importar():
    plugins_dir = './plugins_dir/'
    for plugin_importado in importar(plugins_dir):
        plugin_importado.correr()


#test_importar()
