import numpy as np

arreglo = [[1 + x + j*4 for x in range(4)] for j in range(10)]

arreglo = np.arange(40).reshape(10,4)
#
for fila in range(10):
  for columna in range(4):
    print(f"{arreglo[fila][columna]} ", end='')
    if columna == 1:
      print(f"\t\t", end='')
  print(f"\n", end='')