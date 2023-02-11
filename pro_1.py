def despido(horas):
    if horas<=20:
       print(nombre_trabajador, "Estas despedido por incumplimiendo de horas trabajadas")

nombre_trabajador = input("Ingrese su nombre porfavor")
horas_trabajadas = int(input("Cuántas horas trabajaste"))

if horas_trabajadas==0:
    print("Aqui termina el programa")
    print("Gracias por usarlo")
else:
    print("Turnos")
    print("""1)nocturno 2)diurno""")
    opcion_elegida = int(input("Selecciona tu turno"))
    if opcion_elegida==1:
        print("Tarifa es de 10 pesos")
        sueldo = horas_trabajadas * 10
        print(nombre_trabajador,"Tu sueldo es de: ", sueldo)
        despido(horas_trabajadas)
    elif opcion_elegida==2: 
        print("Tarifa de 20 pesos")
        sueldo = horas_trabajadas * 20
        print(nombre_trabajador, "Tu sueldo es de: ", sueldo)
        despido(horas_trabajadas)
    else:  
       print("Opcion invalida") 


num1 = int(input("Ingresa un número"))
num2 = int(input("Ingresa otro numero"))
multi = num1 * num2
print("La multiplicación de " , num1 ,"*", num2 , "es" , multi)
#print(multi)