try:
  numero1 = int(input("ingrese un numero entero: "))
  numero2 = int(input("ingrese otro numero entero: "))
  division1 = (numero1%numero2)
  if(division1 == 0):
    print("el numero 1 es divisible por el numero 2")
  else:
    print("el numero 1 no es divisible con el numero 2")
  division2 = (numero2%numero1)
  if(division2 == 0):
    print("el numero 2 es divisible por el numero 1")
  else:
    print("el numero 2 no es divisible con el numero 1")
  if(numero1 > numero2):
    print("el numero 1 es mayor")
  elif(numero1 == numero2):
    print("son el mismo numero")
  else:
    print("el numero 2 es mayor")
  if(numero1%2 == 1) and (numero2%2 == 1):
    print("ambos numeros son impares")
except:
    print("numero no valido")