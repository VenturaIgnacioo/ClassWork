def contrasena():  
  #Lee el nombre
  nombre=input("Introduce tu nombre: ")
  #Lee el apellido
  apellido=input("Introduce tu apellido: ")
  #Crea una nueva cadena concateando las tres primeras letras de tu lindo nombre con #las tres primeras letras de tu excelso apellido
  cadena=nombre[0:3]+apellido[0:3]
  #Muestra la nueva cadena
  print("USUARIO: "+cadena)
nuevaCadena=cadena.upper()
  print("En mayusculas: "+ nuevaCadena)
  
  
  contrasena() 
