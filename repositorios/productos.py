import os
import json
import modelos.producto
import configuraciones.constantes


def salva_producto(producto=modelos.producto.Producto()):
    productos=dict()
    if os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url),'r')
        productos = json.load(archivo_productos)
        archivo_productos.close()
    productos[producto.get_codigo()]=producto.__dict__
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url),'w')
    json.dump(productos,archivo_productos)


def busca_por_nombre(nombre=str()):
    archivo_productos=open(os.path.normpath(configuraciones.constantes.base_de_datos_url))
    productos=json.load(archivo_productos)
    for codigo in productos:
        if productos[codigo]['_nombre'] == nombre:
            producto = modelos.producto.Producto()
            producto.convierte_dict_a_producto(productos[codigo])
            return producto
