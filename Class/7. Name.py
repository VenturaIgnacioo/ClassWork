Un programa que lea dos números
#A continuación me pregunta qué deseo hacer
#Me muestra un menú (suma, resta, mult, divi)
#Con lo que elija mando los números a
#una función y lo lo hace (do it)
def mostrarMenu():
  print("***********************************")
  print("*        SUPERCALCULADORA         *")
  print("***********************************")
  print("ELIJA UNA DE LAS SIGUIENTES OPCIONES:")
  print("1. SUMAR")
  print("2. RESTAR")
  print("3. MULTIPLICAR")
  print("4. DIVIDIR")
  print("____________________________________")
  respuesta=input("ELIJA (1, 2, 3 o 4: ")
  return (int(respuesta))

def sumarNumeros(num1,num2):
  respuesta=0
  respuesta=num1+num2
  return(respuesta)

def restarNumeros(num1,num2):
  respuesta=0
  respuesta=num1-num2
  print("EN la funcion respuesta = "+str(respuesta))
  return(respuesta)

def multiplicararNumeros(num1,num2):
  respuesta=0
  respuesta=num1*num2
  return(respuesta)

def dividirNumeros(num1,num2):
  respuesta=0
  respuesta=num1/num2
  return(respuesta)


def calculadora():
  #Leeeeeeo los números
  respuesta=0
  num1 = int(input("Numero 1: "))
  num2 = int(input("numero 2: "))
  #Muestro el menú
  opcion=mostrarMenu()
  #Mando los números a la función elegida
  if(opcion == 1):
    print("Ha elegido sumar ")
    respuesta=sumarNumeros(num1,num2)
  if(opcion==2):
    print("Ha elegido restar ")
    respuesta=restarNumeros(num1,num2)
  if(opcion==3):
    print("Ha elegido multiplicar ")
    respuesta=multiplicarNumeros(num1,num2)
  if(opcion==4):
    print("Ha elegido dividir ")
    respuesta=dividirNumeros(num1,num2)
  #muestro el resultado
  print("Resultado= "+ str(respuesta))

calculadora()
