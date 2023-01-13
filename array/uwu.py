import numpy as np
arreglo = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
for filas in range(3):
  for columnas in range(4):
    arreglo[filas][columnas] = input("ingrese un numero:")
print(arreglo)