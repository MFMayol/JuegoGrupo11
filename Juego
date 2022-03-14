import random

#crea posibles palabras
def nombres():
    palabras = ["leon", "gato","perro","tigre", "jirafa", "elefante" ]
    return palabras

#pregunta si se quiere jugar
def sino():
    print("Bienvenido")
    resp= input("Deseas jugar si/no")
    return resp
    
def palabra():   # eleccion de la palabra
    num = random.randint(0, len(nombres()))
    palabra= list(nombres()[num-1])
    return palabra


def incognita(x):  # creamos lista con los espacios vacios
    list2= []
    for i in range(1,len((x))+1):
        list2.append("_")
    print(list2)
    return list2
     
#se reemplaza las casillas   
def main():
    resp= sino()
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
    
main()
