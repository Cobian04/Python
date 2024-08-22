#Creando una funcion simple
def saludar():
    print("Hola")

#Ejecutando la funcion simple
saludar()

#Creando una funcion con parametro

def nombre(nombre):
    print(f"Tu nombre es {nombre}")

nombre("Jan")

#Creando una funcion que retorne caracteres
def evaluar_numero(n):
    if n > 0:
        return "El número es positivo"
    elif n < 0:
        return "El número es negativo"
    else:
        return "El número es cero"

# Ejemplo de uso
numero = 10
resultado = evaluar_numero(numero)
print(resultado)  # Esto imprimirá "El número es positivo"

numero = -5
resultado = evaluar_numero(numero)
print(resultado)  # Esto imprimirá "El número es negativo"

numero = 0
resultado = evaluar_numero(numero)
print(resultado)  # Esto imprimirá "El número es cero"


