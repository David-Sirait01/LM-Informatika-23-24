#include <iostream>
#include <stdlib.h>
#include <random>
#include <vector>

std::vector<std::vector<int>> multiplyMatrix(const std::vector<std::vector<int>>& mat1, const std::vector<std::vector<int>>& mat2) {
    int row1 = mat1.size();
    int col1 = mat1[0].size();
    int col2 = mat2[0].size();
    
    std::vector<std::vector<int>> result(row1, std::vector<int>(col2, 0));
    
    for (int i = 0; i < row1; i++) {
        for (int j = 0; j < col2; j++) {
            for (int k = 0; k < col1; k++) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
    
    return result;
}

std::vector<std::vector<int>> addition_mtx(const std::vector<std::vector<int>>& matrix1, const std::vector<std::vector<int>>& matrix2) {
    int rows = matrix1.size();
    int cols = matrix1[0].size();

    // Membuat matriks hasil dengan ukuran yang sama
    std::vector<std::vector<int>> result(rows, std::vector<int>(cols, 0));

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            // Melakukan penjumlahan elemen per elemen
            result[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }

    return result;
}

void matrixprinter(const std::vector<std::vector<int>>& matrix) {
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int main(){
    std::vector<std::vector<int>> matrix1 = {
        {5, 2, 1},
        {8, 0, 4},
        {4, 8, 10}
    };

    std::vector<std::vector<int>> matrix2 = {
        {1, 2, 8},
        {6, 1, 3},
        {7, 6, 10}
    };


    std::cout << "Matrix 1 = \n";
    matrixprinter(matrix1);
    std::cout << "\n";
    std::cout << "Matrix 2 = \n";
    matrixprinter(matrix2);

    std::vector<std::vector<int>> result = addition_mtx(matrix1, matrix2);
    std::cout << "\n";
    std::cout << "Matrix 1 + matrix 2 = \n";
    matrixprinter(result);

    std::vector<std::vector<int>> result = multiplyMatrix(matrix1, matrix2)
    std::cout << "\n";
    std::cout << "Matrix 1 * matrix 2 = \n";
    matrixprinter(result);
}