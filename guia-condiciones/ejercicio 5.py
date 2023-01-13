año = int(input("ingrese un año: "))
if(año%4 == 0):
  if(año%100 == 0):
    if(año%400 == 0):
      print("es un año bisiesto uwu")
    else:
      print("no es un año bisiesto:(")
  else:
    print("es un año bisiesto uwu") 
else:
  print("no es un año bisiesto:(")