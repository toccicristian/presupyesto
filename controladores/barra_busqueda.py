import repositorios.productos


def busca(entry_barra, listbox_resultados):
    resultados = repositorios.productos.busca_productos_por_tag_y_conteniendo_en_nombre(entry_barra.get())
    # resultados=repositorios.productos.busca_productos_conteniendo_en_nombre(entry_barra.get())
    listbox_resultados.delete('0', 'end')
    for producto in resultados:
        listbox_resultados.insert('end', producto.get_nombre())
    del resultados


def busca_tview(entry_barra, tview_resultados):
    resultados = repositorios.productos.busca_productos_por_tag_y_conteniendo_en_nombre(entry_barra.get())
    tview_resultados.delete(*tview_resultados.get_children())
    i = 0
    for producto in resultados:
        tview_resultados.insert(parent='', index=i, iid=i, text='', values=(producto.get_nombre(), producto.get_costo()))
        i += 1
    del resultados
