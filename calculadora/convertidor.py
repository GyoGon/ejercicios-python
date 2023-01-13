print("bienvenido a conversiones de cosas")
convertidor = input("que operacion desea realizar? \n 1.Metros a centimetros \n 2.Pulgadas a centimetros \n 3.UF a peso chileno \n :")
if(convertidor == "1"):
  cantidadMetros = int(input("ingrese la cantidad de metros a convertir, debe ser un numero entero: "))
  centimetros = (cantidadMetros * 100)
  print(f"la cantidad de centimetros es de {centimetros}")
elif(convertidor == "2"):
  cantidadPulgadas = int(input("ingrese la cantidad de pulgadas a convertir, debe ser un numero entero: "))
  centimetros = (cantidadPulgadas * 2.54)
  print(f"la cantidad de centimetros es de {centimetros}")
else:
  cantidadUF = int(input("ingrese la cantidad de UF a convertir,debe ser un numero entero: "))
  clp = (cantidadUF * 28713,65)
  print(f"la conversion de uf a clp es de {clp}")
print("gracias por usar nuestro sistema")