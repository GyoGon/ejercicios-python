import funciones as fn
print("Bienvenido al registro civil online del sur")
opcion = 0
while (opcion != 4):
  print(" 1) Agregar Persona \n 2) Buscar Persona \n 3) Sacar certificado \n 4) Salir")
  opcion = int(input("Seleccione una opción: "))
  if(opcion == 1):
    try:
      rut = int(input("Ingrese su rut, sin puntos ni digito verificador: "))
      nombre = input("Ingrese su nombre: ")
      edad = int(input("Ingrese su edad: "))
      fn.agregarPersona(rut, nombre, edad)
      print("Se ha agregado exitosamente")
    except:
      print("Ha ocurrido un problema, intentelo nuevamente")
  if(opcion == 2):
      rut = int(input("Ingrese el rut de la persona que desea buscar: "))
      print(fn.buscarPersona(rut))
  if(opcion == 3):
    certificado = input(" Seleccione que certificado desea sacar \n 1)Nacimiento \n 2)Matrimonio \n 3)Antecedentes \n")
    nombre = input("ingrese su nombre:")
    rut = int(input("ingrese su rut: "))
    print(fn.obtenerCertificado(certificado, nombre, rut))

