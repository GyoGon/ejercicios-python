import numpy as np
from random import randint

prueba = np.array([])

for x in range(100):
  respuesta = randint(1,4)
  if (respuesta == 1):
    respuesta = "a"
  elif (respuesta == 2):
    respuesta = "b"
  elif (respuesta == 3):
    respuesta = "c"
  elif (respuesta == 4):
    respuesta = "d"
  prueba.append(respuesta)
print (prueba)
'''
respuesta = randint(1,4)
for x in range(10):
  for y in range(10):
    prueba[x],[y] = respuesta
print(prueba)
'''
