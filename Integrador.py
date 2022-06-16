#Ejercicio Integrador Parte 1
print ("##### Agro-Sinaloa SA de CV #####")
print ("Sistema de entradas y distribución Version 2.0\n")

cajas_vender = int(input ("Número de cajas a vender: "))
id_prod = input ("ID del producto: ")
venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]
total_producto1 = 0
total_producto2 = 0
total_producto3 = 0

for venta in venta_productos:
  # print(venta[0])
  if venta[0] == 1:
    precio_caja = 285.55
    precio_total = venta[1] * precio_caja
    total_producto1 = total_producto1 + precio_total
    
  elif venta[0] == 2:
    precio_caja = 334.72
    precio_total = venta[1] * precio_caja
    total_producto2 = total_producto2 + precio_total
    
  elif venta[0] == 3:
    precio_caja = 129
    precio_total = venta[1] * precio_caja
    total_producto3 = total_producto3 + precio_total
  
cajas_totales_producto1 = total_producto1/285.55
cajas_totales_producto2 = total_producto2/334.72
cajas_totales_producto3 = total_producto3/129

###VENTA DE MAIZ GRANO####
if id_prod == "1":
  costo_pagar = cajas_vender * 285.55
  print ("\nEl producto es: Maíz Grano")
  print ("El costo por caja es de: 285.55")
  conteo_nuevo_p1 = cajas_vender + cajas_totales_producto1

  
  #######Venta más envío por ser menos de 100 cajas#####
  if cajas_vender <= 100: 
    if conteo_nuevo_p1 < 1500:
      ventacondescuento = (costo_pagar*0.8)+1500
      print ("El costo con descuento de 20% más gastos de envío es:",ventacondescuento)
    else:
      print ("El costo a pagar mas gastos de envío es:",(costo_pagar)+1500)

            
  #######Venta sin costo de envío por ser más de 100 cajas#####
  elif cajas_vender >= 101:
      if conteo_nuevo_p1 < 1500:
        ventacondescuento = (costo_pagar*0.8)
        print ("El costo con descuento de 20% es:",ventacondescuento)
      else:
        print ("El costo por pagar es:",(costo_pagar))




###VENTA DE PEPINO####
elif id_prod == "2":
  costo_pagar = cajas_vender * 334.72
  print ("\nEl producto es: Pepino")
  print ("El costo por caja es de: 334.72")
  conteo_nuevo_p2 = cajas_vender + cajas_totales_producto2

  
  #######Venta más envío por ser menos de 100 cajas#####
  if cajas_vender <= 100: 
    if conteo_nuevo_p2 < 1500:
      ventacondescuento = (costo_pagar*0.8)+1500
      print ("El costo con descuento de 20% más gastos de envío es:",ventacondescuento)
    else:
      print ("El costo a pagar mas gastos de envío es:",(costo_pagar)+1500)

            
  #######Venta sin costo de envío por ser más de 100 cajas#####
  elif cajas_vender >= 101:
      if conteo_nuevo_p2 < 1500:
        ventacondescuento = (costo_pagar*0.8)
        print ("El costo con descuento de 20% es:",ventacondescuento)
      else:
        print ("El costo por pagar es:",(costo_pagar))



  ###VENTA DE TOMATE VERDE####
elif id_prod == "3":
  costo_pagar = cajas_vender * 129
  print ("\nEl producto es: Tomate Verde")
  print ("El costo por caja es de: 129")
  conteo_nuevo_p3 = cajas_vender + cajas_totales_producto3

  
  #######Venta más envío por ser menos de 100 cajas#####
  if cajas_vender <= 100: 
    if conteo_nuevo_p3 < 1500:
      ventacondescuento = (costo_pagar*0.8)+1500
      print ("El costo con descuento de 20% más gastos de envío es:",ventacondescuento)
    else:
      print ("El costo a pagar mas gastos de envío es:",(costo_pagar)+1500)

            
  #######Venta sin costo de envío por ser más de 100 cajas#####
  elif cajas_vender >= 101:
      if conteo_nuevo_p3 < 1500:
        ventacondescuento = (costo_pagar*0.8)
        print ("El costo con descuento de 20% es:",ventacondescuento)
      else:
        print ("El costo por pagar es:",(costo_pagar))

else:
  print("Ingrese una opción válida")
