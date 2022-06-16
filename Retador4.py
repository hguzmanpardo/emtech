#Ejercicio Retador 4
print ("##### Agro-Sinaloa SA de CV #####")
print ("Sistema de entradas y distribución\n")

cajas_vender = int(input ("Número de cajas a vender: "))
id_prod = input ("ID del producto: ")

if id_prod == "1":
  costo_pagar = cajas_vender * 285.55
  print ("\nEl producto es: Maíz Grano")
  print ("El costo de la caja es de: 285.55")
  print ("El costo por pagar es:",costo_pagar)
  
elif id_prod == "2":
  costo_pagar = cajas_vender * 285.55
  print ("\nEl producto es: Pepino")
  print ("El costo de la caja es de: 334.72")
  print ("El costo por pagar es:",costo_pagar)
  
elif id_prod == "3":
  costo_pagar = cajas_vender * 285.55
  print ("\nEl producto es: Pepino")
  print ("El costo de la caja es de: 334.72")
  print ("El costo por pagar es:",costo_pagar)
else:
  print("Ingrese una opción válida")
