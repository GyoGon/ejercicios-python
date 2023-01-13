import numpy as np
a = 0
vector = np.array(["juan","paolo","rosa","anais","leonardo","felipe","pablo","camellia","cristopher","xD"])
while a < 3 :
  print("hola amigos esto es algo de nombres jaja")
  a = int(input("selecciona que opcion quieres realizar: \n 1).Agregar Nombre \n 2).Ver Nombre \n 3).Salir \n"))
  
  if(a == 1):
    nombre = input("ingrese el nombre que desea agregar: ")
    posicion = int(input("en que posicion desea colocarlo: "))
    for x in range(len(vector)):
      np.insert(vector, posicion, nombre)
      vector[posicion] = nombre
  if(a == 2):
    posicion = int(input("que nombre desea ver? ingrese su posicion: "))
    print(vector[posicion])
print(vector)
