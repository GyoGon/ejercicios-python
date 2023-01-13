print("bienvenidos a delivery en cuarentena")
totalBarrosLuco = 0
totalChurrasco = 0
totalCompleto = 0
totalVegetariano = 0
churrasco = input("desea comprar churrascos? si/no:")
if(churrasco == "si"):
  cantidadChurrasco = int(input("cuantos desea llevar?: "))
  totalChurrasco = (cantidadChurrasco * 1500)
completo = input("desea agregar completos? si/no: ")
if(completo == "si"):
  cantidadCompleto = int(input("cuantos desea llevar?: "))
  totalCompleto = (cantidadCompleto * 1000)
vegetariano = input("desea agregar sandwich vegetariano? si/no: ")
if(vegetariano == "si"):
  cantidadVegetariano = int(input("cuantos desea llevar?: "))
  totalVegetariano = (cantidadVegetariano * 2000)
barrosLuco = input("desea agregar barros luco? si/no: ")
if(barrosLuco == "si"):
  cantidadBarrosLuco = int(input("cuantos desea llevar?: "))
  totalBarrosLuco = (cantidadBarrosLuco * 3000)
total = (totalChurrasco + totalCompleto + totalVegetariano + totalBarrosLuco)
descuento = input("tiene un codigo de descuento? si/no: ")
if(descuento == "si"):
  comprobacion = input("escribalo aqui: ")
  total = (total * 0.9)
else:
  total = (total)
print(f"el total de su compra es de {total}")