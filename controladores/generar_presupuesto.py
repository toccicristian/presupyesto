import os
import datetime
import tkinter.filedialog
from fpdf import FPDF
import configuraciones.constantes as const
import controladores.barra_estado as logueador
import utilidades.dinero
from utilidades.archivos import es_archivo,normpath
import repositorios.configuracion as config


def convierte_tview_a_presu(tview):
    presu = list()
    for item in tview.get_children():
        detalle = str(tview.item(item)['values'][1]).encode('latin-1','ignore').decode('latin-1')
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
        if (es_archivo(config.lee_configuracion().get_membrete_url()) and
                config.lee_configuracion().get_membrete_url().endswith(membrete_ext)):
            return config.lee_configuracion().get_membrete_url()
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
        pdf.image(config.lee_configuracion().get_membrete_url(),
                  x=config.lee_configuracion().get_membrete_pos_x(),
                  h=config.lee_configuracion().get_membrete_altura())
    nlinea = 1
    for linea in config.lee_configuracion().get_info():
        pdf.set_font("Courier", size=10)
        pdf.cell(200, 10, txt=(73 - len(linea)) * ' ' + linea, ln=nlinea, align='L')
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
    pdf.cell(200, 10, txt=config.lee_configuracion().get_nota_al_pie() + ' ' * 24, ln=nlinea, align='R')
    pdf.output(normpath(url))
    return True


def generar(tview, barra_estado):
    url_destino = tkinter.filedialog.asksaveasfile(mode='w', filetypes=[('Presupuesto en PDF', '*.pdf')])
    if url_destino is None:
        return False
    if not genera_pdf(convierte_tview_a_presu(tview), url_destino.name):
        logueador.logerror(barra_estado, 'No se pudo generar un presupuesto vacío o el dir. destino no existe.')
        return False
    logueador.log(barra_estado, 'Presupuesto ' + str(os.path.split(url_destino.name)), 'GENERADO')
    return True
