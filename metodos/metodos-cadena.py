cadena1= "holA"
cadena2= "Como estas"

#Convertir a mayusculas
resultado = cadena1.upper()
print(resultado)

#Convertir a minusculas
resultado = cadena1.lower()
print(resultado)

#Primera letra en mayuscula

primer_letra_mayus = cadena1.capitalize()
print(primer_letra_mayus)

#Buscamos una cadena en otra cadena
busqueda_find = cadena1.find("h")
print(busqueda_find) #Muestra la posicion donde se encuentra lo buscado

#Si es numerico devuelve True, de lo contrario devuelve false
es_numerico = cadena1.isnumeric()
print(es_numerico)

#alfanumerico
es_alfa = cadena1.isalpha()
print(es_alfa)

