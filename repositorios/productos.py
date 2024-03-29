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
    productos=dict()
    codigo = configuraciones.constantes.codigo_de_inicio
    productodict = producto.__dict__
    if os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url),'r')
        productos = json.load(archivo_productos)
        archivo_productos.close()
        codigo=configuraciones.constantes.codigo_de_inicio
        if len(productos) > 0:
            codigo=str(int(max(productos))+1).zfill(len(configuraciones.constantes.codigo_de_inicio))
    if int(codigo) > int('9'*len(configuraciones.constantes.codigo_de_inicio)):
        return False
    productodict['_codigo']=codigo
    productos[codigo] = productodict
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url), 'w')
    json.dump(productos, archivo_productos)
    archivo_productos.close()
    return True


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


def marca_producto_como_eliminado(producto_a_marcar=modelos.producto.Producto()):
    producto_a_marcar.set_borrado(True)
    if os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url),'r')
        productos = json.load(archivo_productos)
        archivo_productos.close()
        productos[producto_a_marcar.get_codigo()]=producto_a_marcar.__dict__
        archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url), 'w')
        json.dump(productos, archivo_productos)
        archivo_productos.close()
        return True
    return False


def busca_productos_por_tag_y_conteniendo_en_nombre(cadena=str()):
    if not os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        return list()
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url))
    productos = json.load(archivo_productos)
    resultado_lista_de_productos=list()
    for codigo in productos:
        producto=modelos.producto.Producto()
        producto.convierte_dict_a_producto(productos[codigo])
        if (cadena.upper() in producto.get_nombre().upper() or cadena == '*'
        or all(elem in producto.get_tags() for elem in cadena.upper().split(','))
        ) and not producto.get_borrado():
            resultado_lista_de_productos.append(producto)
        del producto
    return resultado_lista_de_productos


def busca_productos_conteniendo_en_nombre(nombre=str()):
    if not os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        return list()
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
    if not os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        return False
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url))
    productos = json.load(archivo_productos)
    for codigo in productos:
        if productos[codigo]['_nombre'] == nombre and productos[codigo]['_borrado'] is False:
            producto = modelos.producto.Producto()
            producto.convierte_dict_a_producto(productos[codigo])
            return producto
    return False


def busca_por_codigo(codigo_ingresado=str()):
    if not os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        return False
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url))
    productos = json.load(archivo_productos)
    for codigo in productos:
        if productos[codigo]['_codigo'] == codigo_ingresado and productos[codigo]['_borrado'] is False:
            producto = modelos.producto.Producto()
            producto.convierte_dict_a_producto(productos[codigo])
            return producto
    return False


def busca_por_tags(tags_ingresadas=str()):
    if not os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        return list()
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url))
    productos = json.load(archivo_productos)
    resultado = list()
    for codigo in productos:
        if set(tags_ingresadas).issubset(set(productos[codigo]['_tags'])) and productos[codigo]['_borrado'] is False:
            producto_resultado = modelos.producto.Producto()
            producto_resultado.convierte_dict_a_producto(productos[codigo])
            resultado.append(producto_resultado)
    return resultado


def barrer_borrados():
    productos_nueva=dict()
    if os.path.isfile(os.path.normpath(configuraciones.constantes.base_de_datos_url)):
        archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url), 'r')
        productos_dict = json.load(archivo_productos)
        archivo_productos.close()
        cod=configuraciones.constantes.codigo_de_inicio
        for n_producto in productos_dict:
            prod=modelos.producto.Producto()
            prod.convierte_dict_a_producto(productos_dict[n_producto])
            if not prod.get_borrado():
                prod.set_codigo(cod)
                productos_nueva[cod]=prod.__dict__
                cod = str(int(cod)+1).zfill(len(configuraciones.constantes.codigo_de_inicio))
            del prod
    archivo_productos = open(os.path.normpath(configuraciones.constantes.base_de_datos_url), 'w')
    # if productos_nueva:
    #     json.dump(productos_nueva,archivo_productos)
    json.dump(productos_nueva, archivo_productos)
    archivo_productos.close()



