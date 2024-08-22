#Creando una lista con list
lista = list([19, 19])

#Devuelve la cantidad de elementos de la lista
resultado = len(lista)


#Agrega elementos a la lista
agregando_con_append = lista.append("Garcia")


#Agregando elemento a la lista en un indice especifico
lista.insert(0, "Tecnologico Superior De Jalisco")


#Agregando varios elementos a la lista
lista.extend(["hola", False, True, True, False, 1953])


#Eliminando un elemento de la lista
lista.pop(0)

#Eliminando un elemento de la lista por su valor
#lista.remove("jan")

#Eliminando todos los elementos de la lista
#lista.clear

lista.sort()

print(lista)