import numpy as np
from random import randint
arreglo = np.empty([5,3], dtype="<U50")

certificadoNacimiento = randint(1000,5000)
certificadoMatrimonio = randint(1000,5000)
certificadoAntecedentes = randint(1000,5000)
def agregarPersona(rut, nombre, edad):
  if(rut > 1000000 and rut < 99999999):
    if (len(nombre) >= 3):
      if(edad >= 0):
        for i in range(5):
          if(arreglo[i][0] == ''):
            arreglo[i][0] = rut
            arreglo[i][1] = nombre
            arreglo[i][2] = edad
            break
      else:
        return print("La edad no es valida")
    else:
      return print("el nombre es demasiado corto")
  else:
    return print("El rut ingresado no es valido")

def buscarPersona(rut):
  resultado = "la persona no se encuentra registrada"
  for i in range(5):
    if(int(arreglo[i][0]) == rut):
      resultado = f"El rut es : {arreglo[i][0]}, Su nombre es: {arreglo[i][1]}, Su Edad es: {arreglo[i][2]}"
      if(int(arreglo[i][2]) >= 18):
        return resultado, print("Puede sacar permiso para conducir")
      else:
        return print("Aun no puede sacar el permiso de conducir")
      return resultado


def obtenerCertificado(certificado, nombre, rut):
  if(certificado == 1):
    certificado = certificadoNacimiento
    print(f"{nombre} \n Rut: {rut} \n Saco el certificado de: Certificado de nacimiento \n Con valor de:{certificado}")
  if(certificado == 2):
    certificado = certificadoMatrimonio
    print(f"{nombre} \n Rut: {rut} \n Saco el certificado de: Certificado de nacimiento \n Con valor de:{certificado}")
  if(certificado == 3):  
    certificado = certificadoAntecedentes
    print(f"{nombre} \n Rut: {rut} \n Saco el certificado de: Certificado de nacimiento \n Con valor de:{certificado}")


def obtenerArreglo():
    return arreglo

