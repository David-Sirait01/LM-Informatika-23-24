#include <iostream>

int main(){
    int A, B, C;
    std::cout << "Input something\n\n";
    std::cin >> A >> B >> C;
    A = A + B + C;
    B = B + A;
    C = B - A;

    std::cout << "\n\nA = " << A << std::endl;
    std::cout << "\n\nB = " << B << std::endl;
    std::cout << "\n\nC = " << C << std::endl;
    std::cout << "Result = " << (A-B)/C;
    return 0;
}