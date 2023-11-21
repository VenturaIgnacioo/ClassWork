#Este programa lee una contraseña y devuelve si es valida o no.
#La contraseña es valida si cumple con los siguientes requisitos:
#- Más de 8 caracteres.
#- Tiene al menos una letra mayuscula.
#- Tiene al menos una letra minuscula.
#- Tiene al menos un numero.
#- Tiene al menos un caracter especial.
#- No tiene espacios en blanco

def verificaContrasena():
  contrasena=input("Ingrese una contraseña: ")
  validez=True #Defino una variable que me dice si la contraseña es correcta
  #La doy por correcta mientras que no se demuestre lo contrario
  longitud=len(contrasena)
  if(longitud<=8):
    validez=False
  for cont in range(0,longitud):
  if(contraseña.islower() or contraseña.isupper()):
      validez=False
      
