try:
  diaSemana = int(input("ingrese un numero del 1 al 7: "))
  if(diaSemana < 1) or (diaSemana > 7):
    print("el numero ingresado no es valido")
  if(diaSemana == 1):
    print("el numero equivale al dia lunes")
  if(diaSemana == 2):
    print("el numero equivale al dia martes")
  if(diaSemana == 3):
    print("el numero equivale al dia miercoles")
  if(diaSemana == 4):
    print("el numero equivale al dia jueves")
  if(diaSemana == 5):
    print("el numero equivale al dia viernes")
  if(diaSemana == 6):
    print("el numero equivale al dia sabado")
  else:
    print("el numero equivale al dia domingo")
except:
  print("no ha ingresado un numero, intentelo nuevamente")