print("bienvenidos a mascarillas pulentas")
envio = 0
total = 0
cantidad = int(input("cuantas mascarillas desea comprar?"))
total_mascarilla = (cantidad * 500)
comuna = input("de que comuna eres? \n 1.Misma comuna \n 2.Comuna aledaña \n 3.Comuna lejana \n :")
if(comuna == "1"):
  envio = 1000
elif(comuna == "2"):
  envio = 2000
else:
  envio = 3000
if(total_mascarilla > 15000):
  envio = 0
total = (total_mascarilla + envio)
print(f"el total de su compra es de {total}")
print("gracias por preferirnos")