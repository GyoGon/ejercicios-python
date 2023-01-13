totalAPagar = 0
try:
    horasTrabajadas = int(input("Ingrese sus horas trabajadas a la semana: "))

    if(horasTrabajadas > 40):
        totalAPagar = totalAPagar + 124000 + ((horasTrabajadas - 40) * 5100)
    else:
        totalAPagar = horasTrabajadas * 3100

    print(f"El monto total a pagar es de: {totalAPagar} por {horasTrabajadas} Horas")
except:
    print("El valor ingresado no es válido")