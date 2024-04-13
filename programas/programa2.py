# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    match = re.findall(r'"user": "(.*)",', texto)
    diccionario = dict()
    ret = ""
    for item in match:
        if item in diccionario.keys():
            diccionario[item] += 1
        else:
            diccionario[item] = 1

    for item in diccionario.keys():
        ret += item + ': ' + str(diccionario[item]) + '\n'
    #ret = f"{match}"    
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
