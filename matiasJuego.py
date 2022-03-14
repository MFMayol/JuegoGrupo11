#se reemplaza las casillas
def main():
    resp= sino()
    if resp == "si":
      word= palabra()
      final= incognita(word)
      cont=0
      while cont!=len(word):
          letra=input("Dame una letra: ")
          for i in range(0, len(word)):
              if letra==word[i]:
                  final[i]= letra
                  cont=cont+1
              else:
                  cont=cont
          print(final)

      print("Has ganado")
    else:
      resp= sino()

main()
