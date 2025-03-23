def gauss_jordan_solver(matriz, vector):
    n = len(matriz)
    
    # Crear una copia de la matriz para no modificar la original
    matriz_aumentada = [fila[:] for fila in matriz]
    
    # Agregar el vector como una columna adicional en la matriz aumentada
    for i in range(n):
        matriz_aumentada[i].append(vector[i])
    
    # Aplicar el método de Gauss-Jordan
    for i in range(n):
        # Pivoteo parcial: encontrar la fila con el máximo elemento en la columna actual
        max_row = i
        for k in range(i + 1, n):
            if abs(matriz_aumentada[k][i]) > abs(matriz_aumentada[max_row][i]):
                max_row = k
        
        # Intercambiar la fila actual con la fila con el máximo elemento
        matriz_aumentada[i], matriz_aumentada[max_row] = matriz_aumentada[max_row], matriz_aumentada[i]
        
        # Verificar si el pivote es cero (sistema singular)
        if matriz_aumentada[i][i] == 0:
            raise ValueError("El sistema es singular y no tiene solución única.")
        
        # Hacer que el pivote sea 1
        pivot = matriz_aumentada[i][i]
        for j in range(i, n + 1):
            matriz_aumentada[i][j] /= pivot
        
        # Hacer ceros en las otras filas
        for k in range(n):
            if k != i:
                factor = matriz_aumentada[k][i]
                for j in range(i, n + 1):
                    matriz_aumentada[k][j] -= factor * matriz_aumentada[i][j]
    
    # Extraer la solución
    solucion = [matriz_aumentada[i][n] for i in range(n)]
    return solucion

def SolGaussJordan(matriz, vector):
    try:
        # Resolver el sistema
        solucion = gauss_jordan_solver(matriz, vector)

        # Imprimir la solución
        print("Solución del sistema por Gauss-Jordan:")
        for i, x in enumerate(solucion):
            print(f"x{i+1} = {x}")

        # Devolver el vector solución
        print("\nVector solución:")
        print(solucion)
    except ValueError as e:
        print(f"Error: {e}")

""" # ************** Ejemplo de uso ***************
matriz = [
    [4, 0, 0, 0],
    [0, 3, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 1]
]

vector = [8, 6, 4, 2]  # Vector de términos independientes

# Resolver el sistema
solucion = gauss_jordan_solver(matriz, vector)

# Imprimir la solución
print("Solución del sistema por Gauss-Jordan:")
for i, x in enumerate(solucion):
    print(f"x{i+1} = {x}")

# Devolver el vector solución
print("\nVector solución:")
print(solucion) """