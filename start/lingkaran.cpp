#include <cmath>
#include <iostream>

int main(){
    double d, r, l;
    std::cout << "Input jari - jari : ";
    std::cin >> r;

    l = 3.14*pow(r, 2);
    std::cout << "\nLuas = " << l << std::endl;
    system("pause");
}