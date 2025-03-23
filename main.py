import jacobi
import LUmethod
import GaussJordan

Matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Vector = [1, 2, 3, 4]

def intComprobacion(digit):
    try:
        float(digit)
        return digit
    except ValueError:
        return None

def makeMatrixB():
    print("A continuación deberá ingresar los digitos correspondientes a la Matriz b \n ")
    Vector = []
    for digit in range(4):
        d = None
        while d == None:
            d = input("Ingreseel dígito a1"+str(digit)+": ")
            d = intComprobacion(d)
            if d != None:
                Vector.append(d)
            else:
                d = None
    print("Se ha estalecido la matriz b \n ")
    return Vector

def makeMatrix():
    print("A continuación deberá ingresar los dígitos correspondientes a la Matriz A \n ")
    Matrix = []
    for fila in range(4):
        row = []
        print("Fila "+str(fila))
        for digit in range(4):
            d = None
            while d == None:
                d = input("Ingrese el dígito a"+str(fila)+str(digit)+": ")
                d = intComprobacion(d)
                if d != None:
                    row.append(d)
                else:
                    d = None
        Matrix.append(row)
    print("Se ha estalecido la matriz A \n ")
    return Matrix

def userChoices(Matrix, Vector):
    print("Opciones para la resolución del Sistema de Ecuaciones: \n")
    print(" 1- Factoriación LU \n 2- Método de Jacobí \n 3- Gauss-Jordan")
    print(" 4- Imprimir Matriz \n 5- Reemplazar Matrices del Sistema \n")
    option = input("Introduzca la opción que desee aplicar: ").strip()
    if option == "1":
        LUmethod.FactorizacionLU(Matrix, Vector)
    elif option == "2":
        None
    elif option == "3":
        None
    elif option == "4":
        printMatrix()
    elif option == "5":
        Matrix = makeMatrix()
        Vector = makeMatrixB()
    else:
        print("\nSe ha introducido un valor no contemplado. Intentelo de nuevo \n")
        userChoices(Matrix, Vector)

def printMatrix():
    for i in range(4):
        for j in range(4):
            print(str(Matrix[i][j]), end=" ")
        print("| "+str(Vector[i]))

print("Bienvenido \n ")
Matrix = makeMatrix()
Vector = makeMatrixB()
userChoices(Matrix, Vector)
print("Actividad Finalizada \n")