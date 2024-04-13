# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    # Agregar los encabezados
    textoH3 = re.sub(r'###(.*)\\n', r"<h3>\1</h3>\\n", texto)
    textoH2 = re.sub(r'##(.*)\\n', r"<h2>\1</h2>\\n", textoH3)
    textoH1 = re.sub(r'#(.*)\\n', r"<h1>\1</h1>\\n", textoH2)

    textoStrong = re.sub(r'\*\*(.*)\*\*', r"<strong>\1</strong>", textoH1)
    textoEm = re.sub(r'\*(.*)\*', r"<em>\1</em>", textoStrong) 
    textoS = re.sub(r'~~(.*)~~', r"<s>\1</s>", textoEm)

    ret = textoS
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