#Ejercicio Retador 3
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
