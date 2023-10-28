import random as rn
import os, time as t


def printmatrix(matrix):
    ln1 = len(matrix)
    ln2 = len(matrix[0])
    for i in range(0, ln1):
        for j in range(0, ln2):
            print(f"{matrix[i][j]} ", end="")
        print()
    

def addition(matrix1, matrix2):
    # Pastikan kedua matriks memiliki dimensi yang sama
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Matriks tidak dapat dijumlahkan

    rows, cols = len(matrix1), len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

def multiply_matrices(matrix1, matrix2):
    # Mengecek apakah perkalian matriks bisa dilakukan
    if len(matrix1[0]) != len(matrix2):
        return None  # Perkalian tidak mungkin

    # Mendapatkan dimensi matriks hasil
    rows = len(matrix1)
    cols = len(matrix2[0])

    # Inisialisasi matriks hasil dengan nol
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Melakukan perkalian matriks
    for i in range(rows):
        for j in range(cols):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def main():
    matrix1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0, 3):
        for j in range(0, 3):
            matrix1[i][j] = rn.randint(0, 10)
            
    matrix2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0, 3):
        for j in range(0, 3):
            matrix2[i][j] = rn.randint(0, 10)
            
    # print(f"Matrix 1:{printmatrix(matrix1)}")
    # print(f"Matrix 2:{printmatrix(matrix2)}")
    
    print("\nMatrix 1")
    printmatrix(matrix1)
    
    print("\nMatrix 2")
    printmatrix(matrix2)
    
    print("\nMatrix 1 + Matrix 2")
    result = addition(matrix1, matrix2)
    printmatrix(result)

main()
# for i in range(0, 10):
#     main()
#     t.sleep(1)
#     os.system("cls")