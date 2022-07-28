#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import modelos.producto

weburl = 'https://www.diamondcomputacion.com.ar'
verify_ssl=True


def busca_metas_por_id(sopa, id=''):
    resultados=[]
    for meta in sopa.findAll('meta'):
        if 'id=\"'+id+'\"' in str(meta).split():
            resultados.append(meta)
    return resultados


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
    if 'content' not in busca_metas_por_id(sopa, id='descripcionWp')[0].attrs.keys():
        producto.set_existencias(' - OFFLINE -')
        return producto
    producto.set_nombre(str(busca_metas_por_id(sopa,id='tituloWp')[0].attrs['content']).strip())
    producto.set_costo(float(busca_metas_por_id(sopa,id='descripcionWp')[0].attrs['content'].lstrip('Total: $')))
    producto.set_existencias('CONSULTAR DISP. 6061-5749')
    producto.set_urlextra(busca_metas_por_id(sopa,id='imagenWp')[0].attrs['content'].strip().split('?')[0])
    return producto
