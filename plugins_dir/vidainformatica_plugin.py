#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import modelos.producto

weburl = 'https://www.vidainformatica.com.ar' #no olvidar el "www., la pagina no lo suele tener"

#print(f"vidainformatica plugin - Nombres de servicios validos:{'Visita a domicilio x1HS','Armar PC básica desde 0','Armar PC gamer desde 0'}")

def correr(producto=modelos.producto.Producto()):
    verify_ssl=True
    freelance=True
# el nombre del producto debe coincidir con uno de los servicios en esta lista:
#    lista_servicios=["Visita a domicilio x1HS","Armar PC básica desde 0","Armar PC gamer desde 0"]

    for elemento in ['view-source:', 'http://view-source:', 'https://view-source:']:
        if producto.get_producto_url().startswith(elemento):
            producto.set_producto_url(producto.get_producto_url().lstrip(elemento))
    if not producto.get_producto_url().startswith('https://'):
        producto.set_producto_url('https://' + producto.get_producto_url())
    try:
        req = requests.get(producto.get_producto_url(),verify=verify_ssl)
    except requests.exceptions.ConnectionError:
        producto.set_existencias(' - OFFLINE -')
        return producto
    sopa = bs(req.text, 'lxml')
    CONCEPTO_ENCONTRADO=False
    campo_monto=3
    if freelance:
        campo_monto=2

#    if len([servicio for servicio in lista_servicios if servicio.lower() == producto.get_nombre().lower()])>0:
#        for tr in sopa.findAll("tr")[1:]:
#            try:
#                if tr.findAll("td")[0].text.lower() == producto.get_nombre().lower():
#                    producto.set_costo(float(tr.findAll("td")[campo_monto].text))
#                    CONCEPTO_ENCONTRADO=True
#                    producto.set_existencias(" DISPONIBLE ")
#            except IndexError:
#                pass

    for tr in sopa.findAll("tr")[1:]:
        try:
            if tr.findAll("td")[0].text.lower() == producto.get_nombre().lower():
                producto.set_costo(float(tr.findAll("td")[campo_monto].text))
                CONCEPTO_ENCONTRADO=True
                producto.set_existencias(" DISPONIBLE ")
        except IndexError:
            pass


    if not CONCEPTO_ENCONTRADO:
        producto.set_existencias(" - OFFLINE - ")

    return producto
