import modelos.producto
import utilidades.es as es
import datetime
import repositorios.productos


def agregar_producto(tags,nombre,costo,tipo_de_cambio,descripcion,existencias,url,auto):
    if not es.float_o_int(costo.get()) or not es.float_o_int(tipo_de_cambio.get()):
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
    return True


def quitar_producto(cod=str()):
    prod=repositorios.productos.busca_por_codigo(cod)
    if not prod:
        return False
    if not repositorios.productos.elimina_producto(prod):
        return False
    return True
