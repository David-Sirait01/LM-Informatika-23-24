#include <iostream>

const int MAX = 100;

void multiplyMatrix(int mat1[][MAX], int mat2[][MAX], int result[][MAX], int row1, int col1, int col2) {
    for (int i = 0; i < row1; i++) {
        for (int j = 0; j < col2; j++) {
            result[i][j] = 0;
            for (int k = 0; k < col1; k++) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}

void addition_mtx(const int matrix1[3][3], const int matrix2[3][3], int result[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            result[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }
}

void matrixprinter(const int matrix[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    int matrix1[3][3] = {
        {5, 2, 1},
        {8, 0, 4},
        {4, 8, 10}
    };

    int matrix2[3][3] = {
        {1, 2, 8},
        {6, 1, 3},
        {7, 6, 10}
    };

    int result[3][3];

    addition_mtx(matrix1, matrix2, result);

    std::cout << "Matrix 1 = \n";
    matrixprinter(matrix1);
    std::cout << "\n";
    std::cout << "Matrix 2 = \n";
    matrixprinter(matrix2);

    std::cout << "\n";
    std::cout << "Matrix 1 + Matrix 2 = \n";
    matrixprinter(result);

    return 0;
}
