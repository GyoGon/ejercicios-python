print("Bienvenidos a almacenes por ahi")
totalAPagar = 0
try:
  totalCompra = int(input("de cuanto es su compra?: "))
  if(totalCompra > 100000):
    totalAPagar = (totalCompra * 0.8)
    print("aplica descuento")
  else:
    totalAPagar = totalCompra
    print("no aplica descuento")
  print(f"el total a pagar es de {totalAPagar}")
except:
  print("el numero ingresado no es entero")