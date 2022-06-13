def es_float(cadena) -> bool:
    try:
        float(cadena)
        return True
    except ValueError:
        return False


def decimales (num = float(0.0), cantidad_decimales = int(2)):
    return str(int((num-int(num))*(10**cantidad_decimales)))


def float_a_dinero(num=float(0.0),cantidad_decimales=int(2),simbolo=str('$'),separador_decimales=str(','),separador_miles=str('.')):
    entera=str(int(num))
    dinero_entero=''
    cont_dig=0
    for digito in entera[::-1]:
        dinero_entero+=digito
        cont_dig+=1
        if cont_dig == 3:
            dinero_entero+=separador_miles
            cont_dig=0
    dinero_entero=str(dinero_entero[::-1]).lstrip(separador_miles)
    dec=decimales(num, cantidad_decimales)
    if int(decimales(num,cantidad_decimales+1))>4:
        dec=str(int(dec)+1)
    return simbolo+' '+dinero_entero+separador_decimales+dec
