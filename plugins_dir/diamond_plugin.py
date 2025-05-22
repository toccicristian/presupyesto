#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import modelos.producto

weburl = 'https://www.diamondcomputacion.com.ar'


def scrapProductData(sopa, elemento, clase, reemplazar=[]): #reempazar es una lista de tuplas
    resultados=[]
    for elem in sopa.findAll(elemento, attrs={'class':f'{clase}'}):
        for r in reemplazar:
            elem.string=elem.text.replace(r[0],r[1])
        resultados.append(elem)
    return resultados


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
        req = requests.get(producto.get_producto_url())
    except requests.exceptions.ConnectionError:
        producto.set_existencias(' - OFFLINE -')
        return producto
    sopa = bs(req.text, 'lxml')
    if len(scrapProductData(sopa,'span','vtex-store-components-3-x-productBrand'))<1:
        producto.set_existencias(' - OFFLINE -')
        return producto
    producto.set_nombre(str(scrapProductData(sopa,'span','vtex-store-components-3-x-productBrand')[0].text).strip())
    producto.set_costo(float(scrapProductData(sopa,'span','vtex-product-price-1-x-currencyContainer--product',reemplazar=[('$',''),('.',''),(' ',''),(',','.')])[0].text))
    producto.set_existencias('CONSULTAR DISP. 6061-5749')
    return producto
