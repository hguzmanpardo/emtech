respuesta = "1"
while respuesta == "1":
  respuesta = input ("Elige un número: '1 = Ver menú' - '0 = Salir'\n")
  if respuesta == "1":
    print ("### Héctor Saúl Guzmán Pardo ###")
    print ("### Programa Data Analysis ###")
    print ("== Ejercicios Retadores ==")
    ejercicio = input("\nSeleccione un número del 0 al 5:\n 1 - Ejercicio Retador 1 \n 2 - Ejercicio Retador 2\n 3 - Ejercicio Retador 3\n 4 - Ejercicio Retador 4\n 5 - Ejercicio Integrador\n 0 - Regresar\n")
    print("Usted ha seleccionado la opción: ",ejercicio)
    if ejercicio >= "1" and ejercicio <= "5":
    
    
      if ejercicio == "1":
##################################### EJERCICIO RETADOR 1 ######################################
        pob_hom = 1494815
        pob_muj = 1532128
      
        porcien_cul = 33.15
        porcien_maz = 16.57
        temp_media = 25.45
      
        pob_total = pob_hom + pob_muj
        porcien_total_pob = porcien_cul + porcien_maz
      
        print ("Hola, Según información de la Secretaría de Economía   del estado de Sinaloa.")
      
        print ("Se ofrecen los siguientes datos: \n")
      
        print ("La población total entre hombres y mujeres es de:",     pob_total, "habitantes\n")
      
        print ("El porcentaje total de la población entre Culiacán y Mazatlán es de:", porcien_total_pob, "porciento, respectivamente a nivel estado\n")
      
        print ("Además la temperatura anual es de:", temp_media, "grados centigrados\n\n")
      
        print ("Mientras que los tipos de clima que se presentan son: \n")
        print("cálido, subhúmedo, seco y semiseco")
        
        

      elif ejercicio == "2":
##################################### EJERCICIO RETADOR 2 ######################################
        municipios=[]
        habitantes=[]
        municipios.append (input ("Ingresa el 1er municipio: "))
        habitantes.append (int(input ("Cantidad de habitantes: ")))
        
        municipios.append (input ("\nIngresa el 2do municipio: "))
        habitantes.append (int (input ("Cantidad de habitantes: ")))
        
        municipios.append (input ("\nIngresa el 3er municipio: "))
        habitantes.append (int(input ("Cantidad de habitantes: ")))
        print("\n")
        suma_hab = habitantes[0]+habitantes[1]+habitantes[2]
        print("El total de habitantes es de :", suma_hab)
        promedio_hab = suma_hab/3
        print ("El promedio de habitantes es de:", promedio_hab)
##################################### FIN RETADOR 2 ################################
        
        
                      

      elif ejercicio == "3":
##################################### EJERCICIO RETADOR 3 ######################################
        print ("ConstrucArgo esta a sus órdenes para envio de Cemento y Yeso.\n")
        print ("El sistema le atenderá y le notificará sobre el traslado y entrega a domicilio.\n")
        
        cap_max = 3254
        cap_min = cap_max/2
        
        compra_cem = int (input("Cuantos costales de Cemento desea comprar: "))
        compra_yes = int(input("Cuantos costales de Yeso desea comprar: "))
        
        total_kg_cem = compra_cem * 40
        total_kg_yes = compra_yes * 30
        
        kg_totales = total_kg_cem + total_kg_yes
        
        print("Los Kilos totales a entregar son: ", kg_totales)
        
        if kg_totales >= cap_min and kg_totales <= cap_max:
          print("Su pedido es factible para enviar a domicilio.")
        elif kg_totales < cap_min:
          print("Agregue mas sacos para poder enviar a domicilio.")
        elif kg_totales > cap_max:
          print("No es posible enviar a domicilio, excede la capacidad de carga de nuestros vehiculos de entrega.")
##################################### FIN RETADOR 3 ##################################      

    

      elif ejercicio == "4":
##################################### EJERCICIO RETADOR 4 ######################################

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
##################################### FIN RETADOR 4 ######################################
          
      
      elif ejercicio == "5":
##################################### EJERCICIO INTEGRADOR #######################################
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
          
##################################### FIN INTEGRADOR ######################################



  elif respuesta == "0" or ejercicio == "0":
    respuesta = "0"
    print("Gracias por usar esta aplicación!")
    print("Saliendo...")
    break
