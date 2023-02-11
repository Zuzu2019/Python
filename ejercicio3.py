
precio_total = 0
precio = 0
opcion_pedido = []
nombre = []
costo = []
tipo = []

#FUNCIONES
def menu(): 
    print("1: Salsa de chicharron", "$100","Tipo: carne")
    print("2: Biztec encebollado", "$150","Tipo: carne")
    print("3: Albondigas de res en chipotle", "$160", "Tipo: carne")
    print("4: Picadillo de res", "140", "Tipo: carne")
    print("5: Pipian con pollo", "170", "Tipo:carne")
    print("6: Galletas", "$25", "Tipo:postre")
    print("7: Pudin", "$25", "Tipo:postre")
    print("8: Pastel de chocolate", "$35", "Tipo: postre")
    print("9: Vermut", "$100", "Tipo:aperitivo")
    print("10: Mezcal", "$80", "Tipo:aperitivo")
    

def añadir():
  nombre.append(input("Ingrese nombre del platillo: "))
  costo.append(input("Ingrese el precio del plato: "))
  tipo.append(input("Ingrese el tipo de platillo(carne,pescado,aperitivo): "))
  return nombre, costo, tipo

def mostrar():
  print(nombre,costo,tipo)


print("Restaurante: ")
print("Opciones: ")

#menu de opciones
print("1)Realizar pedido","\n","2)Añadir plato","\n","3)Modificar plato" ,"\n","4)Eliminar plato")
opcion_elegida = int(input("Seleccionar opción: "))

if(opcion_elegida==1):
    pedido =  'S'
    while pedido=='S' or pedido=='s':
         print("\n")
         menu()
         opcion_pedido = int(input("Ingrese el numero de platillo que requiere"))
         if opcion_pedido==1:
           precio = 100
         elif opcion_pedido==2:
           precio = 150
         elif opcion_pedido==3:
           precio = 160
         elif opcion_pedido==4:
           precio = 140
         elif opcion_pedido==5:
           precio = 170
         elif opcion_pedido==6:
           precio = 25
         elif opcion_pedido==7:
           precio = 25
         elif opcion_pedido==8:
           precio = 35
         elif opcion_pedido==9:
           precio = 100
         elif opcion_pedido==10:
           precio = 80
         precio_total += precio
         pedido =  input("Si quiere un platillo mas, presione 'S' en caso contrario 'N' ").lower()
elif opcion_elegida==2:
  añadir()
  mostrar()
  menu()

else: 
  print("Fin del programa")
print ("Total a pagar: ", precio_total) 


