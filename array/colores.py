#Crear un Arreglo [3][3][3] manualmente, los valores del arreglo pueden ser “amarillo”, “rojo”, “Naranja”, “Verde” y “Blanco”.

import numpy as np

arregloColores  = np.array(
    [
        [
            ["Amarillo","Naranja","Rojo"],
            ["Blanco","Amarillo","Verde"],
            ["Naranja","Blanco","Rojo"]
        ],
        [
            ["Amarillo","Naranja","Rojo"],
            ["Blanco","Amarillo","Verde"],
            ["Naranja","Blanco","Rojo"]
        ],
        [
            ["Amarillo","Naranja","Rojo"],
            ["Blanco","Amarillo","Rojo"],
            ["Naranja","Blanco","Rojo"]
        ]
    ]
)

contadorAmarillo = 0
contadorRojo = 0
contadorVerde = 0
contadorBlanco = 0
contadorNaranja = 0

for dimension in range(3):
    for fila in range(3):
        for posicion in range(3):
            if(arregloColores[dimension][fila][posicion].upper() == "AMARILLO"):
                contadorAmarillo = contadorAmarillo +1
            elif(arregloColores[dimension][fila][posicion].upper() == "ROJO"):
                contadorRojo = contadorRojo +1
            elif(arregloColores[dimension][fila][posicion].upper() == "VERDE"):
                contadorVerde = contadorVerde +1
            elif(arregloColores[dimension][fila][posicion].upper() == "BLANCO"):
                contadorBlanco = contadorBlanco +1
            elif(arregloColores[dimension][fila][posicion].upper() == "NARANJA"):
                contadorNaranja = contadorNaranja +1

print(f"Número de elementos “amarillo”\t:{contadorAmarillo}")
print(f"Número de elementos “rojo”\t:{contadorRojo}")
print(f"Número de elementos “Naranja”\t:{contadorNaranja}")
print(f"Número de elementos “Verde”\t:{contadorVerde}")
print(f"Número de elementos “Blanco”\t:{contadorBlanco}")