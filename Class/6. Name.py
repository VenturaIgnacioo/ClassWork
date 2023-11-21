#Este proigrama lee una contraseña y devuelve si es válida o no, de acuerdo con
#los siguientes criterios:
# 1.Más de 8 carácteres
# 2.Al menos una letra mayúscula X
# 3.Al menos una letra minúscula X
# 4.Al menos un número
# 5.Al menos un carácter especial X
# 6.No tiene espacios en blanco
#FUNCIONES
def verificaLongitud(contraseña):
  longitud=len(contraseña)
  respuesta=True
  if(longitud<=8):
    respuesta=False
  return(respuesta)


#Programa principal
def verificaContraseña():
  contraseña=input("Ingrese una contraseña: ")
  validez=True #Defino una variable que me dice si es correcta
  #La doy por correcta mientras no se demuestre lo contrario
  verificaLongitud(contraseña)
  verificaMayusculas(contraseña)
  verificaMinusculas(contraseña)
  verificaNumeros(contraseña)
  verificaCaracteresExtraños(contraseña)




  if(contra NO cumple el criterio de contener mayúsculas o minúsculas")
  no_numero=0 #Contar el número de caracteres de la cadena que NO son números
  for cont in range(0,longitud):
    print("El caracter " + str(contraseña[cont]))
    if(contraseña[cont].isnumeric()==False):
       no_numero=no_numero+1
       print(" no es un número")
    else:
      print(" si es un número")
  if(longitud==no_numero):
      validez=False
      print("NO cumple el criterio de contener al menos un número")
  #Finalmente digo si la contraseña es válida o no
  if(validez==True):
    print("Contraseña VÁlIDA")
  else:
    print("Busca otra contraseña")


verificaContraseña()seña.islower() or contraseña.isupper()):
    validez=False
    print("
