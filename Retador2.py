# Ejercicio Retador 2
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
