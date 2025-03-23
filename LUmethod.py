def descomposicion_lu(matriz):
    n = len(matriz)
    L = [[0.0] * n for _ in range(n)]  # Matriz triangular inferior
    U = [[0.0] * n for _ in range(n)]  # Matriz triangular superior
    P = [[float(i == j) for j in range(n)] for i in range(n)]  # Matriz de permutación (inicialmente identidad)

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

    # Copiar la matriz original para no modificarla
    A = [fila[:] for fila in matriz]

    # Descomposición LU con pivoteo parcial
    for i in range(n):
        # Pivoteo parcial: encontrar la fila con el máximo elemento en la columna actual
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        # Intercambiar filas en A, L y P
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            P[i], P[max_row] = P[max_row], P[i]
            if i > 0:
                L[i][:i], L[max_row][:i] = L[max_row][:i], L[i][:i]

        # Verificar si el pivote es cero (sistema singular)
        if A[i][i] == 0:
            raise ValueError("El sistema es singular y no tiene solución única.")

        # Calcular U[i][j] y L[j][i]
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

        # La diagonal de L es 1
        L[i][i] = 1.0

    return P, L, U

def resolver_sistema_lu(P, L, U, b):
    n = len(L)
    y = [0.0] * n  # Vector intermedio y
    x = [0.0] * n  # Solución final x

    # Aplicar la permutación al vector b
    b_permutado = [sum(P[i][j] * b[j] for j in range(n)) for i in range(n)]

    # Resolver Ly = b_permutado (sustitución hacia adelante)
    for i in range(n):
        suma = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b_permutado[i] - suma

    # Resolver Ux = y (sustitución hacia atrás)
    for i in range(n - 1, -1, -1):
        suma = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) / U[i][i]

    return x

# **************Ejemplo de uso****************
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

    # Descomposición LU con matriz de permutación
    P, L, U = descomposicion_lu(matriz)
    print("\nMatriz de permutación P:")
    for fila in P:
        print(fila)
    print("\nMatriz L:")
    for fila in L:
        print(fila)
    print("\nMatriz U:")
    for fila in U:
        print(fila)

    # Resolver el sistema Ax = b
    solucion = resolver_sistema_lu(P, L, U, vector)
    print("\nSolución del sistema por LU:")
    for i, x in enumerate(solucion):
        print(f"x{i+1} = {x}")

except ValueError as e:
    print(f"Error: {e}")