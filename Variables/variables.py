edad = 10
edad +=1
print(edad)

##Concatenacion
nombre = "Jan"
apellido = "Cobian"
nombreCompleto = nombre + " " + apellido
print(nombreCompleto)

##Concatenar con f-String
segundoApellido = "Garcia"
nombreEntero = f"Jan Cobian {segundoApellido}"
print(nombreEntero)

##Operadores de pertenencia 
print("Garcia" in segundoApellido) #True
print("jan" in segundoApellido) #False
print("Hola" not in segundoApellido) #True
