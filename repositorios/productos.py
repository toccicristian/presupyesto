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
    archivo_productos.close()


def crea_producto(producto=modelos.producto.Producto()):
    productos = dict()
    productodict = producto.__dict__
    codigo=configuraciones.constantes.codigo_de_inicio
    if os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url),'r')
        productos = json.load(archivo_productos)
        archivo_productos.close()
        codigo=str(int(max(productos))+1).zfill(len(configuraciones.constantes.codigo_de_inicio))
        if int(codigo) > int('9'*len(configuraciones.constantes.codigo_de_inicio)):
            return False
    productodict['_codigo']=codigo
    productos[codigo] = productodict
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url), 'w')
    json.dump(productos, archivo_productos)
    archivo_productos.close()


def elimina_producto(producto_a_eliminar=modelos.producto.Producto()):
    if os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url),'r')
        productos = json.load(archivo_productos)
        archivo_productos.close()
        productos.pop(producto_a_eliminar.get_codigo())
        archivo_productos=open(os.path.normpath(configuraciones.constantes.base_de_datos_url),'w')
        json.dump(productos,archivo_productos)
        archivo_productos.close()
        return producto_a_eliminar
    return False


def busca_productos_conteniendo_en_nombre(nombre=str()):
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url))
    productos = json.load(archivo_productos)
    resultado_lista_de_productos=list()
    for codigo in productos:
        producto=modelos.producto.Producto()
        producto.convierte_dict_a_producto(productos[codigo])
        if (nombre.upper() in producto.get_nombre().upper() or nombre == '*') and not producto.get_borrado():
            resultado_lista_de_productos.append(producto)
        del producto
    return resultado_lista_de_productos


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
