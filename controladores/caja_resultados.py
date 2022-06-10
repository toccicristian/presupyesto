import repositorios.productos


def presenta_producto_tview(tview_res_busqueda, detalles_tags, detalles_nombre,
                            detalles_costo, detalles_t_cambio, detalles_descripcion,
                            detalles_existencias, detalles_url, auto_var):
    if not tview_res_busqueda.selection():
        return False
    producto = repositorios.productos.busca_por_nombre(tview_res_busqueda.item(tview_res_busqueda.focus())['values'][0])
    if not producto:
        return False
    detalles_tags.delete(0, 'end')
    tagline = ''
    for tag in producto.get_tags():
        tagline += tag + ','
    tagline = tagline.rstrip(',')
    detalles_tags.insert(0, tagline)
    del tagline
    detalles_nombre.delete(0, 'end')
    detalles_nombre.insert(0, producto.get_nombre())
    detalles_costo.delete(0, 'end')
    detalles_costo.insert(0, producto.get_costo())
    detalles_t_cambio.delete(0, 'end')
    detalles_t_cambio.insert(0, producto.get_tipo_de_cambio())
    detalles_descripcion.delete('1.0', 'end')
    detalles_descripcion.insert('1.0', producto.get_descripcion())
    detalles_existencias.delete(0, 'end')
    detalles_existencias.insert(0, producto.get_existencias())
    detalles_url.delete(0, 'end')
    detalles_url.insert(0, producto.get_producto_url())
    auto_var.set(False)
    if producto.get_automatizado():
        auto_var.set(True)
    return True


def presenta_producto(res_busqueda, detalles_tags, detalles_nombre,
                      detalles_costo, detalles_t_cambio, detalles_descripcion,
                      detalles_existencias, detalles_url, auto_var):
    if not res_busqueda.curselection():
        return False
    producto = repositorios.productos.busca_por_nombre(res_busqueda.get(res_busqueda.curselection()))
    detalles_tags.delete(0, 'end')
    tagline = ''
    for tag in producto.get_tags():
        tagline += tag + ','
    tagline = tagline.rstrip(',')
    detalles_tags.insert(0, tagline)
    del tagline
    detalles_nombre.delete(0, 'end')
    detalles_nombre.insert(0, producto.get_nombre())
    detalles_costo.delete(0, 'end')
    detalles_costo.insert(0, producto.get_costo())
    detalles_t_cambio.delete(0, 'end')
    detalles_t_cambio.insert(0, producto.get_tipo_de_cambio())
    detalles_descripcion.delete('1.0', 'end')
    detalles_descripcion.insert('1.0', producto.get_descripcion())
    detalles_existencias.delete(0, 'end')
    detalles_existencias.insert(0, producto.get_existencias())
    detalles_url.delete(0, 'end')
    detalles_url.insert(0, producto.get_producto_url())
    auto_var.set(False)
    if producto.get_automatizado():
        auto_var.set(True)
    return True
