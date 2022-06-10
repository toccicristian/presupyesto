import tkinter

import modelos.producto
import utilidades.es as es
import datetime
import repositorios.productos
import controladores.caja_resultados
import controladores.barra_estado as logueador


def agregar_producto_tview(barra_estado, tags,nombre,costo,tipo_de_cambio,descripcion,existencias,url,auto,tview_res_busqueda):
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
        return False
    tview_res_busqueda.insert(parent='', index=tkinter.END, iid=tkinter.END, text='', values=(prod.get_nombre(), prod.get_costo()))
    tview_res_busqueda.yview_moveto(1)
    logueador.log(barra_estado,prod.get_nombre()+' ', 'AGREGADO')
    return True


def quitar_producto_tview(barra_estado,tview_res_busqueda):
    if not tview_res_busqueda.selection():
        logueador.logerror(barra_estado, 'Nada selecc.')
        return False
    item = tview_res_busqueda.item(tview_res_busqueda.focus())
    prod = repositorios.productos.busca_por_nombre(item['values'][0])
    if not prod:
        logueador.logerror(barra_estado, 'Prod. no existe')
        return False
    if not repositorios.productos.marca_producto_como_eliminado(prod):
        logueador.logerror(barra_estado, 'No se pudo eliminar')
        return False
    tview_res_busqueda.delete(tview_res_busqueda.selection()[0])
    logueador.log(barra_estado, prod.get_nombre()+' ', 'BORRADO')
    return True


def modificar_producto_tview(barra_estado,tview_res_busqueda,
                       tags,nombre,costo,tipo_de_cambio,
                       descripcion,existencias,url,auto):
    if not tview_res_busqueda.selection():
        logueador.logerror(barra_estado,'Nada selecc.')
        return False
    prod_selec = repositorios.productos.busca_por_nombre(tview_res_busqueda.item(tview_res_busqueda.focus())['values'][0])
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
    tview_res_busqueda.item(tview_res_busqueda.selection()[0],
                            text='',
                            values=(prod.get_nombre(), prod.get_costo()*prod.get_tipo_de_cambio()))
    logueador.log(barra_estado,'Producto:'+str(prod.get_codigo())+':'+prod_selec.get_nombre()+': MODIFICADO')


def barrer_borrados(barra_estado):
    repositorios.productos.barrer_borrados()
    logueador.log(barra_estado,'REGISTROS BORRADOS QUITADOS DE BD. REINICIALIZADOS LOS CODIGOS DE PRODUCTO.')
