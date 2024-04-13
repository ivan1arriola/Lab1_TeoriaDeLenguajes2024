# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    match = re.findall(r'"timestamp": "T (.*)",', texto)

    meses = {
        "01": "enero",
        "02": "febrero",
        "03": "marzo",
        "04": "abril",
        "05": "mayo",
        "06": "junio",
        "07": "julio",
        "08": "agosto",
        "09": "septiembre",
        "10": "octubre",
        "11": "noviembre",
        "12": "diciembre"
    }
    ret = ""

    for elem in match:
        fecha = re.findall(r'\d+', elem)
        dd = fecha[2]
        mes = meses[fecha[1]]
        aaaa = fecha[0]
        hh = fecha[3]
        mm = fecha[4]

        fechaStr = dd + " de " + mes + " del " + aaaa + " a las " + hh + ":" +mm + " hs."

        ret += fechaStr + '\n'

    return ret

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)      # ejecutar er
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
