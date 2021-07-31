import os
import json
import modelos.producto
import configuraciones.constantes


def salva_producto(producto=modelos.producto.Producto()):
    productos = dict()
    if os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url), 'r')
        productos = json.load(archivo_productos)
        archivo_productos.close()
    productos[producto.get_codigo()] = producto.__dict__
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url), 'w')
    json.dump(productos, archivo_productos)


def crea_producto(producto=modelos.producto.Producto()):
    productos = dict()
    productodict = dict()
    productodict = producto.__dict__
    codigo=configuraciones.constantes.codigo_de_inicio
    if os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url),'r')
        productos = json.load(archivo_productos)
        archivo_productos.close()
        codigo=str(len(productos)).zfill(len(configuraciones.constantes.codigo_de_inicio))
    productodict['_codigo']=codigo
    productos[codigo] = productodict
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url), 'w')
    json.dump(productos, archivo_productos)


def busca_por_nombre(nombre=str()):
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url))
    productos = json.load(archivo_productos)
    for codigo in productos:
        if productos[codigo]['_nombre'] == nombre and productos[codigo]['_borrado'] is False:
            producto = modelos.producto.Producto()
            producto.convierte_dict_a_producto(productos[codigo])
            return producto
    return False


def busca_por_codigo(codigo_ingresado=str()):
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url))
    productos = json.load(archivo_productos)
    for codigo in productos:
        if productos[codigo]['_codigo'] == codigo_ingresado and productos[codigo]['_borrado'] is False:
            producto = modelos.producto.Producto()
            producto.convierte_dict_a_producto(productos[codigo])
            return producto
    return False


def busca_por_tags(tags_ingresadas=str()):
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url))
    productos = json.load(archivo_productos)
    resultado = list()
    for codigo in productos:
        if set(tags_ingresadas).issubset(set(productos[codigo]['_tags'])) and productos[codigo]['_borrado'] is False:
            producto_resultado = modelos.producto.Producto()
            producto_resultado.convierte_dict_a_producto(productos[codigo])
            resultado.append(producto_resultado)
    return resultado
