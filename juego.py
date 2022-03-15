
def restart():
  plus = str(input("Quieres repetir el juego? "))
  if plus == "si":
    print("Adivina la palabra")
    juego()
    restart()
    
  else:
    print("Que mal ;(")
