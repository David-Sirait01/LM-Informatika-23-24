#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    double a, b;
    std::vector<double> var = {0,0,0,0};
    std::cout << "Input 2 angka : ";
    std::cin >> a >> b;

    var[0] = a+b;
    var[1] = a-b;
    var[2] = a*b;
    var[3] = a/b;

    std::cout << "Angka pertama\t = " << a << std::endl;
    std::cout << "Angka kedua\t = " << b;

    std::cout << std::endl << std::endl;
    std::cout << "Penjumlahan -> " << var[0] << std::endl;
    std::cout << "Pengurangan -> " << var[1] << std::endl;
    std::cout << "Perkalian   -> " << var[2] << std::endl;
    std::cout << "Pembagian   -> " << var[3] << std::endl;

    return 0;

    system("pause");
}
