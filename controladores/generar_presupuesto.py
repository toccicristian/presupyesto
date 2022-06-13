import os
import datetime
import tkinter.filedialog
from fpdf import FPDF
import configuraciones.constantes as const
import controladores.barra_estado as logueador
import utilidades.dinero


def convierte_tview_a_presu(tview):
    presu = list()
    for item in tview.get_children():
        detalle = tview.item(item)['values'][1]
        cantidad = tview.item(item)['values'][2]
        costo = ''
        separador = ''
        if utilidades.dinero.es_float(str(tview.item(item)['values'][3])):
            costo = str(utilidades.dinero.float_a_dinero(float(tview.item(item)['values'][3]))).rjust(14)
            separador = ' : '
        presu.append(str(detalle).ljust(50) + separador +
                     str(cantidad).rjust(3) + separador +
                     costo)
    return presu


def membrete_url():
    for membrete_ext in const.membrete_extensiones:
        if os.path.isfile(os.path.expanduser(os.path.normpath(const.membrete_url + membrete_ext))):
            return os.path.expanduser(os.path.normpath(const.membrete_url + membrete_ext))
    return False


def genera_pdf(datos=None, url='/.'):
    if datos is None:
        return False
    if not os.path.isdir(os.path.split(os.path.expanduser(os.path.normpath(url)))[0]):
        return False
    fecha = str(datetime.datetime.now().strftime('%d/%m/%Y'))
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=15)
    if membrete_url():
        pdf.image(membrete_url(), x=const.membrete_pos_x, h=const.membrete_height)
    nlinea = 1
    for dato_razon_social in [const.razon_social, const.datos_razon_social_linea1, const.datos_razon_social_linea2,
                              const.datos_razon_social_linea3]:
        pdf.set_font("Courier", size=10)
        pdf.cell(200, 10, txt=(73 - len(dato_razon_social)) * ' ' + dato_razon_social, ln=nlinea, align='L')
        nlinea += 1
    pdf.set_font("Courier", size=15)
    pdf.cell(200, 10, txt=fecha, ln=nlinea, align='L')
    nlinea += 1
    pdf.cell(200, 10, txt='PRESUPUESTO', ln=nlinea, align='C')
    pdf.set_font("Courier", size=10)
    nlinea += 1
    for linea in datos:
        pdf.cell(200, 10, txt=linea, ln=nlinea, align='L')
        nlinea += 1
    pdf.set_font("Courier", size=8)
    pdf.cell(200, 10, txt=const.nota_al_pie + ' ' * 24, ln=nlinea, align='R')
    pdf.output(os.path.expanduser(os.path.normpath(url)))
    return True


def generar(tview, barra_estado):
    url_destino = tkinter.filedialog.asksaveasfile(mode='w', filetypes=[('Presupuesto en PDF', '*.pdf')]).name
    if not genera_pdf(convierte_tview_a_presu(tview), url_destino):
        logueador.logerror(barra_estado, 'No se pudo generar un presupuesto vacío o el dir. destino no existe.')
        return False
    logueador.log(barra_estado, 'Presupuesto ' + str(os.path.split(url_destino)), 'GENERADO')
    return True
