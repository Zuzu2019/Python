#funciones del programa

def opciones():
    print("1)Realizar pedido","\n","2)Añadir plato","\n","3)Modificar plato" ,"\n","4)Eliminar plato")
def menu(nombre, precio, tipo):
    for x in listadeprecios:
        nombre.append(input("ingrese el nombre del plato: "))
        precio.append(float(input("Ingrese el precio del plato: ")))
        tipo.append(input("ingrese el tipo del plato: "))
        return nombre, precio, tipo
def anadir(nombre, precio, tipo):
    seguir = input("Desea actulizar el menu? s/n: ".lower())
    while (seguir == "s"):
        nombre.append(input("ingrese el nombre del plato: "))
        precio.append(float(input("Ingrese el precio del plato: ")))            
        tipo.append(input("ingrese el tipo del plato: "))
        seguir = input("Quiere ingresar otro plato? s/n: ").lower()
        return nombre, precio, tipo
def eliminar():
    seguir = input("Desea eliminar un plato? s/n: ".lower())
    while (seguir == "s"):
        plato_a_eliminar = input("ingrese el nombre del plato a eliminar: ")
        posicion = nombre.index(plato_a_eliminar)
        nombre.remove(plato_a_eliminar)
        precio.pop(posicion)
        tipo.pop(posicion)
        seguir = input("Desea eliminar otro plato? s/n: ".lower())
def modificar():
    seguir = input("Desea modificar el menu? s/n: ".lower())
    while (seguir == "s"):
        plato_a_modificar = input("ingrese el plato a modificar: ")
        posicion = nombre.index(plato_a_modificar)
        nombre[posicion] = input("ingrese el nombre del plato: ")
        precio[posicion] = float(input("ingrese el precio del plato: "))
        tipo[posicion] = input("ingrese el tipo de plato: ")
        seguir = input("Quiere modificar otro plato? s/n: ").lower()
def pedidos(numero_mesa):
    seguir  = 's'
    total = 0
    while(seguir=='s'):
        pedido = input("Que desea ordenar?: ")
        if pedido in nombre:
            posicion = nombre.index(pedido)
            total = total + precio[posicion]
            seguir = input("Quiere pedir algo mas? s/n: ").lower()
        else:
            print("Te pido disculpas, nos quedamos sin ", pedido)
    print("Su ticket es de: ", total)



#PROGRAMA PRINCIPAL
nombre = []
precio = []
tipo = []
listadeprecios = 5
#menu de opciones
menu(nombre, precio, tipo)
opciones()
opcion_elegida = int(input("Seleccionar opción: "))
if(opcion_elegida==2):
    anadir(nombre,precio,tipo)
elif(opcion_elegida==1):
    pedidos(1)
elif(opcion_elegida==3):
    modificar()
elif(opcion_elegida==4):
    eliminar()
else:
    print("Fin del programa: ")

