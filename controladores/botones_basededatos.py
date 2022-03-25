import tkinter

import modelos.producto
import utilidades.es as es
import datetime
import repositorios.productos
import controladores.caja_resultados
import controladores.barra_estado as logueador


def agregar_producto(barra_estado, tags,nombre,costo,tipo_de_cambio,descripcion,existencias,url,auto,res_busqueda):
    if not es.float_o_int(costo.get()) or not es.float_o_int(tipo_de_cambio.get()):
        logueador.logerror(barra_estado,'Monto no numerico')
        return False
    if repositorios.productos.busca_por_nombre(nombre.get()):
        logueador.logerror(barra_estado, 'Producto ya existe')
        return False
    prod=modelos.producto.Producto()
    prod.set_automatizado(bool(auto.get()))
    prod.set_borrado(False)
    prod.set_producto_url(str(url.get()))
    for tag in tags.get().split(','):
        prod.add_tag(str(tag.upper()))
    prod.set_nombre(str(nombre.get()))
    prod.set_descripcion(str(descripcion.get('1.0','end')))
    prod.set_costo(float(costo.get()))
    prod.set_ultima_actualizacion_de_costo(str(datetime.date.today().strftime('%Y%m%d%H%M')))
    prod.set_tipo_de_cambio(float(tipo_de_cambio.get()))
    prod.set_existencias(str(existencias.get()).upper())
    prod.set_urlextra('url1')
    prod.set_urlextra2('url2')
    if not (repositorios.productos.crea_producto(prod)):
        logueador.logerror(barra_estado,'BASE DE DATOS LLENA. NO SE PUDO AGREGAR '+str(prod.get_nombre()))
    res_busqueda.insert('end',prod.get_nombre())
    logueador.log(barra_estado,prod.get_nombre()+' ','AGREGADO')
    return True


def quitar_producto(barra_estado,detalles_tags,detalles_nombre,detalles_costo,
                    detalles_t_cambio,detalles_descripcion,detalles_existencias,
                    detalles_url,auto_var,res_busqueda):
    if not res_busqueda.curselection():
        logueador.logerror(barra_estado,'Nada selecc.')
        return False
    prod = repositorios.productos.busca_por_nombre(res_busqueda.get(res_busqueda.curselection()))
    if not prod:
        logueador.logerror(barra_estado, 'Prod. no existe')
        return False
    if not repositorios.productos.marca_producto_como_eliminado(prod):
        logueador.logerror(barra_estado, 'No se pudo eliminar')
        return False
    old_selection=res_busqueda.curselection()
    res_busqueda.delete(res_busqueda.curselection())
    res_busqueda.selection_clear(0,'end')
    res_busqueda.selection_set(old_selection[0])
    if old_selection[0]==res_busqueda.size():
        res_busqueda.selection_set(res_busqueda.size()-1)
    res_busqueda.see('end')
    logueador.log(barra_estado,prod.get_nombre()+' ','BORRADO')
    controladores.caja_resultados.presenta_producto(res_busqueda,detalles_tags,detalles_nombre,
                                                    detalles_costo,detalles_t_cambio,detalles_descripcion,
                                                    detalles_existencias,detalles_url,auto_var)
    return True


def modificar_producto(barra_estado,res_busqueda,
                       tags,nombre,costo,tipo_de_cambio,
                       descripcion,existencias,url,auto):
    if not res_busqueda.curselection():
        logueador.logerror(barra_estado,'Nada selecc.')
        return False
    prod_selec = repositorios.productos.busca_por_nombre(res_busqueda.get(res_busqueda.curselection()))
    if not prod_selec:
        logueador.logerror(barra_estado, 'Producto no existe')
        return False
    if not es.float_o_int(costo.get()) or not es.float_o_int(tipo_de_cambio.get()):
        logueador.logerror(barra_estado,'Monto no numerico')
        return False
    prod=modelos.producto.Producto()
    prod.set_automatizado(bool(auto.get()))
    prod.set_borrado(False)
    prod.set_producto_url(str(url.get()))
    for tag in tags.get().split(','):
        prod.add_tag(str(tag.upper()))
    prod.set_nombre(str(nombre.get()))
    prod.set_descripcion(str(descripcion.get('1.0','end')))
    prod.set_costo(float(costo.get()))
    prod.set_ultima_actualizacion_de_costo(str(datetime.date.today().strftime('%Y%m%d%H%M')))
    prod.set_tipo_de_cambio(float(tipo_de_cambio.get()))
    prod.set_existencias(str(existencias.get()).upper())
    prod.set_urlextra('url1')
    prod.set_urlextra2('url2')
    prod.set_codigo(prod_selec.get_codigo())
    if (repositorios.productos.busca_por_nombre(prod.get_nombre())
            and repositorios.productos.busca_por_nombre(prod.get_nombre()).get_codigo() != prod.get_codigo()):
        logueador.logerror(barra_estado,'Ya existe '+str(prod.get_nombre()+'; Elegir otro.'))
        return False
    repositorios.productos.salva_producto(prod)
    old_selection=res_busqueda.curselection()
    res_busqueda.delete(res_busqueda.curselection())
    res_busqueda.selection_clear(0,'end')
    res_busqueda.insert(old_selection[0],prod.get_nombre())
    res_busqueda.selection_set(old_selection[0])
    logueador.log(barra_estado,'Producto:'+str(prod.get_codigo())+':'+prod_selec.get_nombre()+': MODIFICADO')


def barrer_borrados(barra_estado):
    repositorios.productos.barrer_borrados()
    logueador.log(barra_estado,'REGISTROS BORRADOS QUITADOS DE BD. REINICIALIZADOS LOS CODIGOS DE PRODUCTO.')
