num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
num3 = int(input("ingrese el ultimo numero: "))
if(num1 == num2+num3):
  print(f"el numero {num1} es igual a la suma de {num2} y {num3}")
if(num2 == num1+num3):
  print(f"el numero {num2} es igual a la suma de {num1} y {num3}")
if(num3 == num1+num2):
  print(f"el numero {num3} es igual a la suma de {num1} y {num2}")
print(f"la suma de los numeros es {num1+num2+num3}")