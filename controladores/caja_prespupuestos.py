import tkinter
import configuraciones.constantes as const
import repositorios.productos


def inserta_total(tview_presu, total=float(0.0)):
    tview_presu.insert('', tkinter.END, values=('*', 150 * '*', ' ', ' '))
    tview_presu.insert('', tkinter.END, values=('*', 'TOTAL '.rjust(30), ' ', round(total, 2)))


def inicializa(tview_presu):
    tview_presu.delete(*tview_presu.get_children())
    inserta_total(tview_presu, float(0.0))


def presenta_presupuesto(tview_presu, lista_items=None):
    if lista_items is None:
        lista_items = list()
    tview_presu.delete(*tview_presu.get_children())
    subtotal = float(0.0)
    for item in lista_items:
        tview_presu.insert('', tkinter.END, values=(item[0], item[1], item[2], round(float(item[3]), 2)))
        subtotal += float(item[3])
    inserta_total(tview_presu, total=subtotal)


def devuelve_diccionario_de_items(tview_presu):
    diccionario_de_items = dict()
    for item in tview_presu.get_children():
        if str(tview_presu.item(item)['values'][0]) != '*':
            diccionario_de_items[str(tview_presu.item(item)['values'][0]).zfill(len(const.codigo_de_inicio))] = {
                'codigo': str(tview_presu.item(item)['values'][0]).zfill(len(const.codigo_de_inicio)),
                'detalle': tview_presu.item(item)['values'][1],
                'cantidad': tview_presu.item(item)['values'][2],
                'costo': tview_presu.item(item)['values'][3]}
    return diccionario_de_items


def agrega_item(tview_presu, prod):
    diccionario_de_items = devuelve_diccionario_de_items(tview_presu)
    item_dict = {'codigo': str(prod.get_codigo()),
                 'detalle': str(prod.get_nombre()),
                 'cantidad': '1',
                 'costo': float(prod.get_costo()) * float(prod.get_tipo_de_cambio())}
    if item_dict['codigo'] in diccionario_de_items:
        item_dict['cantidad'] = (str(int(item_dict['cantidad']) +
                                     int(diccionario_de_items[item_dict['codigo']]['cantidad'])))
        item_dict['costo'] = item_dict['costo'] + float(diccionario_de_items[item_dict['codigo']]['costo'])
    diccionario_de_items[item_dict['codigo']] = item_dict
    lista_de_items = list()
    for codigo in diccionario_de_items:
        lista_de_items.append((diccionario_de_items[codigo]['codigo'],
                               diccionario_de_items[codigo]['detalle'],
                               diccionario_de_items[codigo]['cantidad'],
                               diccionario_de_items[codigo]['costo']))
    presenta_presupuesto(tview_presu, lista_de_items)


def quita_item(tview_presu):
    if not tview_presu.selection():
        return False
    prod = repositorios.productos.busca_por_codigo(
        str(tview_presu.item(tview_presu.selection()[0])['values'][0]).zfill(len(const.codigo_de_inicio)))
    nuevo_costo = float(prod.get_costo()) * float(prod.get_tipo_de_cambio()) * (float(
        tview_presu.item(tview_presu.selection()[0])['values'][2]) - 1)
    tview_presu.item(tview_presu.selection()[0],
                     values=(str(tview_presu.item(tview_presu.selection()[0])['values'][0]
                                 ).zfill(len(const.codigo_de_inicio)),
                             tview_presu.item(tview_presu.selection()[0])['values'][1],
                             str(int(tview_presu.item(tview_presu.selection()[0])['values'][2]) - 1),
                             round(nuevo_costo,2)))
    tview_presu.item(tview_presu.get_children()[-1],
                     values=('*', 'TOTAL '.rjust(30), ' ',
                             round(float(tview_presu.item(tview_presu.get_children()[-1])['values'][3]) - (
                                     float(prod.get_costo()) * float(prod.get_tipo_de_cambio())), 2)))
    if int(tview_presu.item(tview_presu.selection()[0])['values'][2]) == 0:
        tview_presu.delete(tview_presu.selection()[0])
    return True
