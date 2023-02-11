#Declaracion de listas donde van ser almacenados los datos
nombres = []
edades = []
sexo = []

tamaño = 4
mayoresM = 0
mayoresF = 0
menoresF = 0
menoresM = 0
a = 0
b = 0
c = 0
d = 0

for i in range(tamaño):
    nombre = input("Ingrese su nombre completo: ")
    edad = int(input("Ingresa edad: "))
    print("Sexo")
    print("1) Masculino, 2) Femenino")
    opcion_elegida = int(input("Selecciona una opción (1 o 2): "))

    nombres.append(nombre)
    edades.append(edad)
    sexo.append(opcion_elegida)


#Mostrar los datos insertados 
print("Lista de personas insertadas: ")
for i in range(tamaño):
    #print("Persona: ", i + 1)
    #print(nombre[i])
    print("Lista de personas: ")
    print("Nombre: ", nombres[i])
    print("Edad: ", edades[i])
    print("Sexo: ", sexo[i])
    if (edades[i]>=18 and sexo[i]==1):
        mayoresM = a + 1
        #print("Numero de personas mayores masculinos a 18 años son: ", mayoresM)
    elif(edades[i]<18 and sexo[i]==1):
        menoresM = b + 1
    elif(edades[i]<18 and sexo[i]==2):
        menoresF = c + 1
       # print("Numero de personas menores de 18 años femeninas son: ", menoresF)
    elif(edades[i]>=18 and sexo[i]==2):
        mayoresF = d + 1
    else:
       print("")    
personas_mayores = mayoresM + mayoresF
personas_menores = menoresF + menoresM

print("Cantidad de personas mayores son: ", personas_mayores)
print("Cantidad de personas menores son: ", personas_menores)

Total_personas = personas_mayores + personas_menores

porcentaje_menores = 100 * (personas_menores/Total_personas)
porcentaje_mayores = 100 * (personas_mayores/Total_personas)



print("Porcentaje de personas mayores son: ", porcentaje_mayores , "%")
print("Porcentaje de personas menores son: ", porcentaje_menores, "%")





