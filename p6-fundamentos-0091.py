# Ejemplo 1: Variables básicas
# Ian Gutierrez NC 0091

nombre = "Carlos"
edad = 18
altura = 1.75

print(nombre)
print(edad)
print(altura)


# Ejemplo 2: Cambiar el valor de una variable

x = 10
print(x)

x = 20
print(x)

x = 30
print(x)


# Ejemplo 3: Variables de diferentes tipos

nombre = "Ana"
edad = 20
estudiante = True

print("Nombre:", nombre)
print("Edad:", edad)
print("¿Es estudiante?:", estudiante)


# 2. Múltiples variables

# Ejemplo 1: Asignar varios valores

nombre, edad, ciudad = "Luis", 21, "Chihuahua"

print(nombre)
print(edad)
print(ciudad)


# Ejemplo 2: Mismo valor para varias variables

x = y = z = 100

print(x)
print(y)
print(z)


# Ejemplo 3: Intercambiar valores

a = 5
b = 10

print("Antes:")
print("a =", a)
print("b =", b)

a, b = b, a

print("Después:")
print("a =", a)
print("b =", b)


# 3. Tipos de datos

# Ejemplo 1: String, Integer y Float

nombre = "Pedro"
edad = 25
precio = 99.99

print(nombre)
print(edad)
print(precio)

print(type(nombre))
print(type(edad))
print(type(precio))


# Ejemplo 2: Boolean

mayor_de_edad = True
tiene_licencia = False

print(mayor_de_edad)
print(tiene_licencia)

print(type(mayor_de_edad))
print(type(tiene_licencia))


# Ejemplo 3: List, Tuple y Dictionary

frutas = ["manzana", "banana", "naranja"]

colores = ("rojo", "verde", "azul")

persona = {
    "nombre": "Juan",
    "edad": 22
}

print(frutas)
print(colores)
print(persona)


# 4. Operadores aritméticos

# Ejemplo 1: Suma y resta

a = 20
b = 5

suma = a + b
resta = a - b

print("Suma:", suma)
print("Resta:", resta)


# Ejemplo 2: Multiplicación y división

a = 10
b = 2

multiplicacion = a * b
division = a / b

print("Multiplicación:", multiplicacion)
print("División:", division)


# Ejemplo 3: Módulo, exponente y división entera

a = 10
b = 3

print("Módulo:", a % b)
print("Exponente:", a ** b)
print("División entera:", a // b)


# 5. Operadores de comparación

# Ejemplo 1: Igual y diferente

a = 10
b = 10

print(a == b)
print(a != b)


# Ejemplo 2: Mayor y menor

a = 20
b = 10

print("¿a es mayor que b?", a > b)
print("¿a es menor que b?", a < b)


# Ejemplo 3: Mayor o igual y menor o igual

edad = 18

print("¿Es mayor o igual a 18?", edad >= 18)
print("¿Es menor o igual a 18?", edad <= 18)


# 6. Operadores lógicos

# Ejemplo 1: and

edad = 20
tiene_identificacion = True

resultado = edad >= 18 and tiene_identificacion

print(resultado)


# Ejemplo 2: or

edad = 16
tiene_permiso = True

resultado = edad >= 18 or tiene_permiso

print(resultado)


# Ejemplo 3: not

es_menor = False

print(es_menor)
print(not es_menor)


# Datos del alumno

print("Programa realizado por Ian Gutierrez NC = 0091")
