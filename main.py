import jacobi
import LUmethod
import GaussJordan

Matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8], 
          [9, 10, 11, 12], 
          [13, 14, 15, 16]]

Vector = [1, 2, 3, 4]
a = None

# Función para comprobar que los valores ingresados son números reales
def intComprobacion(digit):
    try:
        float(digit)
        return digit
    except ValueError:
        print("\033[31mEl valor ingresado no es un número válido\n\033[0m")
        return None

# Función para la creación de la matriz b
def makeMatrixB():
    print("A continuación deberá ingresar los digitos correspondientes a la Matriz b \n ")
    Vector = []
    for digit in range(4):
        d = None
        while d == None:
            d = input("Ingreseel dígito a1"+str(digit)+": ").strip()
            d = intComprobacion(d)
            if d != None:
                d=float(d)
                Vector.append(d)
            else:
                d = None
    print("Se ha estalecido la matriz b \n ")
    return Vector

# Función para la creación de la matriz A
def makeMatrix():
    print("A continuación deberá ingresar los dígitos correspondientes a la Matriz A \n ")
    Matrix = []
    for fila in range(4):
        row = []
        print("Fila "+str(fila))
        for digit in range(4):
            d = None
            while d == None:
                d = input("Ingrese el dígito a"+str(fila)+str(digit)+": ").strip()
                d = intComprobacion(d)
                if d != None:
                    d=float(d)
                    row.append(d)
                else:
                    d = None
        Matrix.append(row)
    print("Se ha estalecido la matriz A \n ")
    return Matrix

# Función para comprobar si la matriz es una matriz identidad o una matriz nula
def matrixComprobacion(Matrix, Vector, a):
    Null = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    Id = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    if Matrix == Null:
        print("\033[31mEl Sistema ingresado es nulo. Porfavor ingrese un nuevo sistema\n\033[0m")
        Matrix = makeMatrix()
        Vector = makeMatrixB()
    elif Matrix == Id:
        print("\nLa matriz A ingresada corresponde a la matriz identidad. Se presentan los resultados: ")
        print("X1 = "+str(Vector[0]))
        print("X2 = "+str(Vector[1]))
        print("X3 = "+str(Vector[2]))
        print("X4 = "+str(Vector[3]))
        c = input("¿Desea continuar con la matriz identidad? \ny/n: ").strip()
        if c == "y":
            a = 0
        else:
            if c != "n":
                print("\033[31mSe ha ingresado un valor no contemplado\n\033[0m")
            print("\nPorfavor ingrese un nuevo sistema ")
            Matrix = makeMatrix()
            Vector = makeMatrixB()
    else:
        a = 0
    return Matrix, Vector, a

# Menú de selección de opciones
def userChoices(Matrix, Vector, a):
    print("\nOpciones para la resolución del Sistema de Ecuaciones: \n")
    print(" 1- Factoriación LU \n 2- Método de Jacobí \n 3- Gauss-Jordan")
    print(" 4- Imprimir Matriz \n 5- Reemplazar Matrices del Sistema \n")
    print(" 6- Salir \n")
    option = input("Introduzca la opción que desee aplicar: \n").strip()
    if option == "1":
        LUmethod.FactorizacionLU(Matrix, Vector)
    elif option == "2":
        jacobi.SolJacobi(Matrix, Vector)
    elif option == "3":
        GaussJordan.SolGaussJordan(Matrix, Vector)
    elif option == "4":
        printMatrix(Matrix, Vector)
    elif option == "5":
        Matrix = makeMatrix()
        Vector = makeMatrixB()
    elif option == "6":
        a = 1
    else:
        print("\033[31m\nSe ha introducido un valor no contemplado. Intentelo de nuevo\n\033[0m")
        return userChoices(Matrix, Vector, a)
    return Matrix, Vector, a

#Función para imprimir la matriz 4x4
def printMatrix(Matrix, Vector):
    for i in range(4):
        for j in range(4):
            print(str(Matrix[i][j]), end="  ")
        print("| "+str(Vector[i]))

#  CÓDIGO DE EJECUCIÓN DEL PROGRAMA
print("Bienvenido \n ")
Matrix = makeMatrix()
Vector = makeMatrixB()
a = 1
while a == 1:
    Matrix, Vector, a = matrixComprobacion(Matrix, Vector, a)
a = 0
while a == 0:
    Matrix, Vector, a = userChoices(Matrix, Vector, a)
print("Actividad Finalizada \n")