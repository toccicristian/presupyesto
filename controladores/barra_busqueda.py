import repositorios.productos


def busca (entry_barra,listbox_resultados):
    resultados=repositorios.productos.busca_productos_conteniendo_en_nombre(entry_barra.get())
    listbox_resultados.delete('0','end')
    for producto in resultados:
        listbox_resultados.insert('end',producto.get_nombre())
    del resultados