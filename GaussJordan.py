def gauss_jordan_solver(matriz, vector):
    n = len(matriz)
    
    # Crear la matriz aumentada [matriz | vector]
    for i in range(n):
        matriz[i].append(vector[i])
    
    # Aplicar el método de Gauss-Jordan
    for i in range(n):
        # Pivoteo parcial: encontrar la fila con el máximo elemento en la columna actual
        max_row = i
        for k in range(i + 1, n):
            if abs(matriz[k][i]) > abs(matriz[max_row][i]):
                max_row = k
        
        # Intercambiar la fila actual con la fila con el máximo elemento
        matriz[i], matriz[max_row] = matriz[max_row], matriz[i]
        
        # Verificar si el pivote es cero (sistema singular)
        if matriz[i][i] == 0:
            raise ValueError("El sistema es singular y no tiene solución única.")
        
        # Hacer que el pivote sea 1
        pivot = matriz[i][i]
        for j in range(i, n + 1):
            matriz[i][j] /= pivot
        
        # Hacer ceros en las otras filas
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(i, n + 1):
                    matriz[k][j] -= factor * matriz[i][j]
    
    # Extraer la solución
    solucion = [matriz[i][n] for i in range(n)]
    return solucion

# ************** Ejemplo de uso ***************
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
print(solucion)