numPulsaciones = 0
sexo = " "
while(sexo.lower() != "f" or sexo.lower() != "m"):
  sexo = input("ingrese su sexo (F)emenino/(M)asculino: ")
  edad = int(input("ingrese su edad: "))
  if(sexo.lower() == "f") or (sexo.lower() == "m"):
    if(sexo.lower() == "f"):
      numPulsaciones = ((220 - edad)/10)
      print(f"el numero de pulsaciones que debe tener es de {numPulsaciones}")
    if(sexo.lower() == "m"):
      numPulsaciones = ((210 - edad)/10)
      print(f"el numero de pulsaciones que debe tener es de {numPulsaciones}")