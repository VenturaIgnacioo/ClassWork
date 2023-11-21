#Este programa cuenta el numero de aes que tiene una palabra
def cuenta_aes():
   #Leemos una palabra
  palabra = input("Dime una palabra: ")
  #Inicializamos la variable que almacenará el numero de aes
  numeroAes=0
  #Recorremos la palabra y preguntamos si la letra es una a
  for cont in for cont in ranger(0,len(palabra)):
    if palabra[cont] == "A":
       numeroAes = numeroAes + 1
  #Mostramos el numero de aes contadas
  
  print("La palabra"+palabra+"tiene"+str(numeroAes)+" aes")
  

cuenta_aes()
