import math

# Funciones matemáticas
def suma(num1, num2): return num1 + num2
def resta(num1, num2): return num1 - num2
def multiplicacion(num1, num2): return num1 * num2
def division(divisor, dividendo): return divisor / dividendo
def potenciacion(base, exp): return base ** exp
def raizcuadrada(rad, precision): 
    if rad < 0:
        return "La raíz cuadrada de un número negativo no está definida"
    estimacion = rad
    while abs(estimacion * estimacion - rad) > precision:
        estimacion = 0.5 * (estimacion + rad / estimacion)
    return estimacion
def factorial(numero): return 1 if numero == 0 else numero * factorial(numero - 1)

# Funciones trigonométricas usando la serie de Taylor
def seno(radianes, terminos): 
    return sum([((-1)**n) * (radianes**(2*n+1)) / factorial(2*n+1) for n in range(terminos)])

def coseno(radianes, terminos): 
    return sum([((-1)**n) * (radianes**(2*n)) / factorial(2*n) for n in range(terminos)])

def tangente(radianes, terminos): 
    return seno(radianes, terminos) / coseno(radianes, terminos)

# Funciones estadísticas
def promedio(muestra): return sum(muestra) / len(muestra)
def varianza(muestra): 
    prom = promedio(muestra)
    return sum((x - prom) ** 2 for x in muestra) / (len(muestra) - 1)
def desviacion_estandar(muestra): return raizcuadrada(varianza(muestra), 1e-10)

# Funciones de matrices
def leer_matriz(longitud):
    return [[int(input(f"Ingrese el dato de la fila {i+1}, columna {j+1}: ")) for j in range(longitud)] for i in range(longitud)]

def sumamatrices(matA, matB): return [[matA[i][j] + matB[i][j] for j in range(len(matA[0]))] for i in range(len(matA))]
def restamatrices(matA, matB): return [[matA[i][j] - matB[i][j] for j in range(len(matA[0]))] for i in range(len(matA))]
def multiplicarmatrices(matA, matB): 
    return [[sum(matA[i][k] * matB[k][j] for k in range(len(matB))) for j in range(len(matB[0]))] for i in range(len(matA))]
def determinante2x2(mat): return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

# Menú de opciones
def menu():
    print("1. Operaciones básicas aritméticas")
    print("2. Funciones trigonométricas")
    print("3. Operaciones con matrices")
    print("4. Estadística Descriptiva")
    print("Cualquier otro número: Salir")
    return int(input("Ingrese una selección: "))

def operaciones_basicas():
    print("1. Sumar 2 números\n2. Restar 2 números\n3. Multiplicar 2 números\n4. Dividir 2 números\n5. Potenciación\n6. Raíz Cuadrada\n7. Factorial\n8. Salir")
    return int(input("Elija la operación: "))

def trigonometria():
    print("1. Seno\n2. Coseno\n3. Tangente\nCualquier otro número: Salir")
    return int(input("Elija la función trigonométrica: "))

def matrices():
    print("1. Suma de matrices\n2. Resta de matrices\n3. Multiplicación de matrices\n4. Determinante 2x2\nCualquier otro número: Salir")
    return int(input("Elija la operación con matrices: "))

def estadistica():
    print("1. Promedio\n2. Desviación estándar\n3. Varianza\nCualquier otro número: Salir")
    return int(input("Elija la operación estadística: "))

# Funciones para ejecutar cada opción del menú
def ejecutar_operaciones_basicas():
    opcion = operaciones_basicas()
    if opcion == 1:
        num1, num2 = int(input("Primer número: ")), int(input("Segundo número: ")); print(f"Suma: {suma(num1, num2)}")
    elif opcion == 2:
        num1, num2 = int(input("Primer número: ")), int(input("Segundo número: ")); print(f"Resta: {resta(num1, num2)}")
    elif opcion == 3:
        num1, num2 = int(input("Primer número: ")), int(input("Segundo número: ")); print(f"Multiplicación: {multiplicacion(num1, num2)}")
    elif opcion == 4:
        num1, num2 = int(input("Divisor: ")), int(input("Dividendo: ")); print(f"División: {division(num1, num2)}")
    elif opcion == 5:
        base, exp = int(input("Base: ")), int(input("Exponente: ")); print(f"Potenciación: {potenciacion(base, exp)}")
    elif opcion == 6:
        rad, precision = int(input("Radicando: ")), float(input("Precisión: ")); print(f"Raíz cuadrada: {raizcuadrada(rad, precision)}")
    elif opcion == 7:
        numero = int(input("Número: ")); print(f"Factorial: {factorial(numero)}")

def ejecutar_trigonometria():
    opcion = trigonometria()
    if opcion in [1, 2, 3]:
        x = float(input("Ángulo en grados: "))
        terminos = int(input("Número de términos: "))
        x_rad = math.radians(x)  # Convierte el ángulo a radianes
        if opcion == 1:
            print(f"Seno: {seno(x_rad, terminos)}")
        elif opcion == 2:
            print(f"Coseno: {coseno(x_rad, terminos)}")
        elif opcion == 3:
            print(f"Tangente: {tangente(x_rad, terminos)}")

def ejecutar_matrices():
    opcion = matrices()
    if opcion in [1, 2]:
        longitud = int(input("Tamaño de la matriz: "))
        print("Matriz A:")
        matA = leer_matriz(longitud)
        print("Matriz B:")
        matB = leer_matriz(longitud)
        if opcion == 1:
            print(f"Suma: {sumamatrices(matA, matB)}")
        elif opcion == 2:
            print(f"Resta: {restamatrices(matA, matB)}")
    elif opcion == 3:
        longitud = int(input("Tamaño de la matriz: "))
        print("Matriz A:")
        matA = leer_matriz(longitud)
        print("Matriz B:")
        matB = leer_matriz(longitud)
        print(f"Multiplicación: {multiplicarmatrices(matA, matB)}")
    elif opcion == 4:
        mat = []
        print("Matriz 2x2:")
        for i in range(2):
            mat.append([int(input(f"Ingrese dato [{i+1},{j+1}]: ")) for j in range(2)])
        print(f"Determinante: {determinante2x2(mat)}")

def ejecutar_estadistica():
    opcion = estadistica()
    muestra = [int(input(f"Ingrese el dato {i+1}: ")) for i in range(int(input("Tamaño de la muestra: ")))]
    if opcion == 1:
        print(f"Promedio: {promedio(muestra)}")
    elif opcion == 2:
        print(f"Desviación estándar: {desviacion_estandar(muestra)}")
    elif opcion == 3:
        print(f"Varianza: {varianza(muestra)}")

# Programa principal
while True:
    seleccion = menu()
    if seleccion == 1:
        ejecutar_operaciones_basicas()
    elif seleccion == 2:
        ejecutar_trigonometria()
    elif seleccion == 3:
        ejecutar_matrices()
    elif seleccion == 4:
        ejecutar_estadistica()
    else:
        print("Saliendo del programa...")
        break
