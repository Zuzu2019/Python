menu=[
    [1, "Salsa de chicharron", "100","carne"],
    [2, "Biztec encebollado", "150","carne"],
    [3, "Albondigas de res en chipotle", "$160", "carne"],
    [4, "Picadillo de res", "140", "carne"],
    [5, "Pipian con pollo", "170", "carne"],
    [6, "Galletas", "$25", "postre"],
    [7, "Pudin", "$25", "postre"],
    [8, "Pastel de chocolate", "$35", "postre"],
    [9, "Vermut", "$100", "aperitivo"],
    [10, "Mezcal", "$80", "aperitivo"],
    ]

def findAndReplace(menu_completo, id_a_cambiar, nuevoValor):

    for item_menu in menu_completo:
        if(item_menu[0]==id_a_cambiar):
            item_menu=nuevoValor


def anadir(lista:list, lista2:list):
    lista.append(lista2)

def eliminar(lista: list, lista_eliminar:list):
    lista.remove(lista_eliminar)

    

edit=input('Indique el Valor que quiere cambiar: ')
if edit in menu:
            #newValue = input(f'Por que valor desea cambiar al numero {edit}: ')
            n_nombre=input("ingrese nombre")
            n_precio=input("ingrese precio")
            n_tipo=input("ingrese tipo")
            newValue=[len(menu)+1,n_nombre, n_precio, n_tipo]
            findAndReplace(menu,edit,newValue)
            print('Se ha cambiado exitosamente')
else :
         print('No se encuentra el numero en la Lista, intente nuevamente.')



item=[11, "ensalada de puñetazos", 32, "postre"]
#anadir(menu, item)

#eliminar(menu, menu[0])

for i in menu:
    print(i)