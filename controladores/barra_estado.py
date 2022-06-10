

def log (barraestado,mensaje=str(),sufijo=str()):
    sufijomax=int(int(barraestado.cget('width'))*40/100)
    if len(sufijo)>sufijomax:
        sufijo=sufijo[0:sufijomax-1]
    mensajemax=int(barraestado.cget('width'))-sufijomax
    if len(mensaje)> mensajemax:
        mensaje=mensaje[0:mensajemax-4]+'...'
    barraestado.config(text=mensaje+sufijo,bg='#000fff000')


def logerror(barraestado,mensaje=str()):
    if len(mensaje)>barraestado.cget('width'):
        mensaje=mensaje[0:barraestado.cget('width')-4]+'...'
    barraestado.config(text=mensaje,bg='#ff0000')
