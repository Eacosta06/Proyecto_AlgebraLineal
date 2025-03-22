def descomposicion_lu(matriz):
    n = len(matriz)
    L = [[0.0] * n for _ in range(n)]  # Matriz triangular inferior
    U = [[0.0] * n for _ in range(n)]  # Matriz triangular superior

    # Verificar que la matriz no sea singular (determinante no sea cero)
    def determinante(mat):
        if len(mat) != len(mat[0]):
            raise ValueError("La matriz no es cuadrada.")
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for c in range(len(mat)):
            submat = [fila[:c] + fila[c+1:] for fila in mat[1:]]
            det += ((-1) ** c) * mat[0][c] * determinante(submat)
        return det

    if determinante(matriz) == 0:
        raise ValueError("La matriz es singular (no tiene inversa).")

    # Descomposición LU utilizando el método alternativo
    for i in range(n):
        # Inicializar la diagonal de L con 1.0
        L[i][i] = 1.0

        # Matriz U (triangular superior)
        for k in range(i, n):
            suma = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = matriz[i][k] - suma

        # Matriz L (triangular inferior)
        for k in range(i + 1, n):
            suma = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (matriz[k][i] - suma) / U[i][i]

    return L, U

def resolver_sistema_lu(L, U, b):
    n = len(L)
    y = [0.0] * n  # Vector intermedio y
    x = [0.0] * n  # Solución final x

    # Resolver Ly = b (sustitución hacia adelante)
    for i in range(n):
        suma = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b[i] - suma

    # Resolver Ux = y (sustitución hacia atrás)
    for i in range(n - 1, -1, -1):
        suma = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) / U[i][i]

    return x

# Ejemplo de uso
try:
    # Definir la matriz A y el vector b
    matriz = [
        [4, 1, 2, 3],
        [1, 5, 3, 2],
        [2, 3, 6, 1],
        [3, 2, 1, 7]
    ]
    vector = [10, 11, 12, 13]  # Vector de términos independientes

    # Imprimir la matriz A
    print("Matriz A:")
    for fila in matriz:
        print(fila)

    # Imprimir la matriz aumentada [A | b]
    print("\nMatriz aumentada [A | b]:")
    for i in range(len(matriz)):
        print(matriz[i] + [vector[i]])

    # Descomposición LU
    L, U = descomposicion_lu(matriz)
    print("\nMatriz L:")
    for fila in L:
        print(fila)
    print("\nMatriz U:")
    for fila in U:
        print(fila)

    # Resolver el sistema Ax = b
    solucion = resolver_sistema_lu(L, U, vector)
    print("\nSolución del sistema:")
    for i, x in enumerate(solucion):
        print(f"x{i+1} = {x}")

except ValueError as e:
    print(f"Error: {e}")