import funciones as fn

print("Bienvenido  a nuestro Sistema de Registro de Productos 2000+")

opcion = 0

while(opcion !=5):
  print("1) Agregar Producto")
  print("2) Eliminar Producto")
  print("3) Buscar Producto")
  print("4) Ver Productos")
  print("5) Salir")
  opcion = int(input("Seleccione una opción: "))

  if(opcion == 1):
    codigo = input("Ingrese un Código para el Producto: ")
    producto = input("Ingrese un Nombre para el Producto: ")
    precio = input("Ingrese un Precio para el Producto: ")
    fn.agregarProducto(codigo, producto, precio)
  elif(opcion == 2):
    codigo = input("Ingrese el codigo del producto que desee eliminar: ")
    fn.eliminarProducto(codigo)
  elif(opcion == 3):
    codigo = input("Ingrese un código para buscar: ")
    print(fn.buscarProducto(codigo))
  elif(opcion == 4):
    print(fn.obtenerArreglo())