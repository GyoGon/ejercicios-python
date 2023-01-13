def suma(n1,n2):
  return n1+n2
def resta(n1,n2):
  return n1-n2
def multi(n1,n2):
  return n1*n2
def division(n1,n2):
  return n1/n2
def resto(n1,n2):
  return n1%n2

import numpy as np

arreglo = np.empty([5,3], dtype="<U50")

def agregarProducto(codigo, producto, precio):
    for i in range(5):
        if(arreglo[i][0] == ''):
            arreglo[i][0] = codigo
            arreglo[i][1] = producto
            arreglo[i][2] = precio
            break

def obtenerArreglo():
    return arreglo

def eliminarProducto(codigo):
  for i in range(5):
    if(arreglo[i][0] == codigo):
      arreglo[i][0] = ''
      arreglo[i][1] = ''
      arreglo[i][2] = ''
      break
def buscarProducto(codigo):
    resultado = "El producto NO existe"
    for i in range(5):
        if(arreglo[i][0] == codigo):
            resultado = "El producto SI existe"
            break

    return resultado