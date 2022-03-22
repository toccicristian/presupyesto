import modelos.producto
import utilidades.es as es
import datetime
import repositorios.productos
import controladores.barra_estado as logueador


def agregar_producto(barra_estado, tags,nombre,costo,tipo_de_cambio,descripcion,existencias,url,auto):
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
    repositorios.productos.crea_producto(prod)
    logueador.log(barra_estado,prod.get_nombre()+' ','AGREGADO')
    return True


def quitar_producto(barra_estado,res_busqueda):
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
    res_busqueda.delete(res_busqueda.curselection())
    logueador.log(barra_estado,prod.get_nombre()+' ','BORRADO')
    return True
