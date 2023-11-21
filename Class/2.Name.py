def tabla():
  n_tabla = input("¿Que tabla quieres escribir?: ")
  print("TABLA DEL " + str(n_tabla))
  for cont in range(1,10):
    print(str(n_tabla)+" x "+ str(cont)+" = "+str(int(n_tabla)*cont) )
  


tabla()(
