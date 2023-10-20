#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import modelos.producto

weburl = 'https://www.diamondcomputacion.com.ar'
verify_ssl=True


def correr(producto=modelos.producto.Producto()):
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
    if len(sopa.findAll('meta', attrs={'property': 'product:price:amount'}))==0:
        producto.set_existencias(' - OFFLINE -')
        return producto
    producto.set_nombre(str( sopa.findAll('span', attrs={'class' : 'vtex-breadcrumb-1-x-term ph2 c-on-base'})[0].text ).strip())
    producto.set_costo(float( sopa.findAll('meta', attrs={'property': 'product:price:amount'})[0].get('content') ))
    producto.set_existencias('CONSULTAR DISP. 6061-5749')
    producto.set_urlextra( sopa.findAll('meta', attrs={'property':'og:image'})[0].get('content').split('?')[0] )
    return producto
