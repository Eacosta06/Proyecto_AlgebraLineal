import main

def es_diagonalmente_dominante(matriz):
    """
    Verifica si una matriz es estrictamente diagonalmente dominante.
    """
    n = len(matriz)
    for i in range(n):
        suma_fila = sum(abs(matriz[i][j]) for j in range(n) if j != i)
        if abs(matriz[i][i]) <= suma_fila:
            return False
    return True

def reordenar_filas(matriz, vector):
    """
    Reordena las filas de la matriz y el vector para que la matriz sea estrictamente diagonalmente dominante.
    """
    n = len(matriz)
    for i in range(n):
        # Encontrar la fila con el máximo elemento en la columna i
        max_row = i
        for k in range(i + 1, n):
            if abs(matriz[k][i]) > abs(matriz[max_row][i]):
                max_row = k
        
        # Intercambiar filas en la matriz y el vector
        if max_row != i:
            matriz[i], matriz[max_row] = matriz[max_row], matriz[i]
            vector[i], vector[max_row] = vector[max_row], vector[i]
    main.printMatrix(matriz, vector)
    return matriz, vector

def metodo_jacobi(matriz, vector, tol=1e-10, max_iter=1000):
    """
    Resuelve un sistema de ecuaciones lineales utilizando el método de Jacobi.
    Si la matriz no es estrictamente diagonalmente dominante, reordena las filas.
    """
    n = len(matriz)
    
    # Verificar si la matriz es estrictamente diagonalmente dominante
    if not es_diagonalmente_dominante(matriz):
        print("La matriz no es estrictamente diagonalmente dominante. Reordenando filas...")
        matriz, vector = reordenar_filas(matriz, vector)
        if not es_diagonalmente_dominante(matriz):
            raise ValueError("No se pudo reordenar la matriz para que sea estrictamente diagonalmente dominante.")
    
    # Inicializar el vector solución
    x = [0.0] * n
    
    # Iterar hasta convergencia o alcanzar el máximo de iteraciones
    for iteracion in range(max_iter):
        x_nuevo = [0.0] * n
        for i in range(n):
            suma = sum(matriz[i][j] * x[j] for j in range(n) if j != i)
            x_nuevo[i] = (vector[i] - suma) / matriz[i][i]
        
        # Verificar convergencia
        if all(abs(x_nuevo[i] - x[i]) < tol for i in range(n)):
            print(f"Convergencia alcanzada en {iteracion + 1} iteraciones.")
            return x_nuevo
        
        x = x_nuevo
    
    print("Advertencia: No se alcanzó la convergencia en el número máximo de iteraciones.")
    return x

def SolJacobi(matriz, vector):
    try:
        # Resolver el sistema utilizando el método de Jacobi
        solucion = metodo_jacobi(matriz, vector)
        print("\nSolución del sistema por Jacobi:")
        for i, x in enumerate(solucion):
            print(f"x{i+1} = {x}")

    except ValueError as e:
        print(f"Error: {e}")

""" # Ejemplo de uso
try:
    # Definir la matriz A y el vector b
    matriz = [
        [6, 1, 2, 1],
        [1, 11, 3, 4],
        [2, 3, 9, 3],
        [3, 2, 4, 10]
    ]
    vector = [10, 19, 17, 19]  # Vector de términos independientes

    # Resolver el sistema utilizando el método de Jacobi
    solucion = metodo_jacobi(matriz, vector)
    print("\nSolución del sistema por Jacobi:")
    for i, x in enumerate(solucion):
        print(f"x{i+1} = {x}")

except ValueError as e:
    print(f"Error: {e}") """