#lista donde se guarda los datos de los trabajadores
nomina_total=0

def despido(nombre, hrs):
    if hrs<=20:
       print(nombre, "Estas despedido por incumplimiendo de horas trabajadas")

nombres = []
horas = []
turno = []

tamaño = int(input("¿Cuántos trabajadores ingresaras?"))

for i in range(tamaño):
    nombre_trabajador = input("Ingrese su nombre porfavor")
    horas_trabajadas = int(input("Cuántas horas trabajaste"))
    nombres.append(nombre_trabajador)
    horas.append(horas_trabajadas)
    if horas_trabajadas==0:
        print("Aqui termina el programa")
        print("Gracias por usar este programa")
    else:
        print("Turnos")
        print("""1)nocturno 2)diurno""")
        opcion_elegida = int(input("Selecciona tu turno"))
        turno.append(opcion_elegida) 

    #mostrar las listas
    print("Lista de trabajadores: ")
for i in range(tamaño):
    print("\n")
    print("Trabajador", i + 1)
    print("Nombre: ", nombres[i])
    if turno[i]==1:
            print("horas: ", horas[i])
            print("Tarifa es de 10 pesos")
            sueldo = horas[i] * 10
            print("Total a recibir: ", sueldo)
            despido(nombres[i], horas[i])
    elif turno[i]==2: 
            print("horas: ", horas[i])
            print("Tarifa de 20 pesos X hora")
            sueldo = horas[i] * 20
            print("Total a recibir: ", sueldo)
            despido(nombres[i], horas[i])
    else:  
        print("Opcion invalida")
    print("turno: ", turno[i])
    nomina_total += sueldo
print("\n")
print("Nomina total: ", nomina_total)







 