#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import modelos.producto

weburl = 'https://www.aikencomputacion.com.ar'
verify_ssl=True

def correr(producto=modelos.producto.Producto()):
    for elemento in ['view-source:', 'http://view-source:', 'https://view-source:']:
        if producto.get_producto_url().startswith(elemento):
            producto.set_producto_url(producto.get_producto_url().lstrip(elemento))
    if not producto.get_producto_url().startswith('https://'):
        producto.set_producto_url('https://' + producto.get_producto_url())
    try:
        req = requests.get(producto.get_producto_url(), verify=verify_ssl)
    except requests.exceptions.ConnectionError:
        producto.set_existencias(' - OFFLINE -')
        return producto
    sopa = bs(req.text, 'lxml')
    if sopa.find('div', attrs={'id': 'tab1'}) is None or len(sopa.find('div', attrs={'id': 'tab1'}).text.strip()) == 0:
        producto.set_existencias(' - OFFLINE -')
        return producto
    producto.set_nombre(sopa.find('div', attrs={'id': 'tab1'}).text.strip())
    if sopa.find('h3', attrs={'class': 'product-price'}) is not None:
        producto.set_costo(float(sopa.find('h3', attrs={'class': 'product-price'}).text.strip().lstrip('$ ')))
    for i in range(1, 11):
        if sopa.find('span', attrs={'class': 'stock_color_' + str(i) + ' product-available'}) is not None:
            producto.set_existencias(
                sopa.find('span', attrs={'class': 'stock_color_' + str(i) + ' product-available'}).text)
    producto.set_urlextra('')
    imagen_subdir = '/bytedata/foto/'
    imagen_identificador = 'src=\"' + imagen_subdir
    if sopa.findAll('img') is not None:
        imagen_resultados = []
        for img in sopa.findAll('img'):
            if imagen_identificador in str(img) and producto.get_nombre() in str(img):
                imagen_resultados.append(str(img))
        if len(imagen_resultados) > 0:
            producto.set_urlextra(
                weburl + imagen_subdir + imagen_resultados[0].split(imagen_identificador)[1].rstrip('\"/>'))
    return producto
