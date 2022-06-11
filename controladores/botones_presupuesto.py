import controladores.caja_prespupuestos
import repositorios.productos
import controladores.barra_estado as logueador


def agrega_item(tview_presu, tview_resultados, barra_de_estado):
    prod = repositorios.productos.busca_por_nombre(tview_resultados.item(tview_resultados.focus())['values'][0])
    if not prod:
        logueador.logerror(barra_de_estado, 'No hay un item seleccionado en la caja de búsquedas.')
        return False
    controladores.caja_prespupuestos.agrega_item(tview_presu, prod)
    logueador.log(barra_de_estado,str(prod.get_nombre())+' ', 'AGREGADO A PRESUPUESTO')


def quita_item(tview_presu, barra_de_estado):
    if not tview_presu.selection() or tview_presu.item(tview_presu.selection()[0])['values'][0] == '*':
        logueador.logerror(barra_de_estado, 'No hay un item seleccionado en la caja de presupuestos')
        return False
    nombre_item = tview_presu.item(tview_presu.selection()[0])['values'][1]
    if not controladores.caja_prespupuestos.quita_item(tview_presu):
        logueador.logerror(barra_de_estado, 'No hay un item seleccionado en la caja de presupuestos.')
        return False
    logueador.log(barra_de_estado,str(nombre_item)+' ', 'QUITADO DE PRESUPUESTO')
