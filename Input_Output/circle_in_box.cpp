#include <iostream>
#include <cmath>

int main(int argc, char const *argv[])
{
    double s;
    double var[3];
    std::cout << "sisi =\n>>> ";
    std::cin >> s;
    /*
        var[0] = luas persegi
        var[1] = r
        var[2] = luas lingkaran
        var[3] = L.lingkaran - L.persegi
    */
    
    // Hitung luas persegi
    var[0] = pow(s, 2);

    // Cari jari-jari; S = D, r = D/2
    // jari-jari (r)
    var[1] = s/2;

    // Luas lingkaran = phi * r^2
    var[2] = M_PI * pow(var[1], 2);
    
    // Luas persegi - Luas lingkaran
    var[3] = var[0] - var[2];

    std::cout << "Luas persegi   = " << var[0] << std::endl;
    std::cout << "Luas lingkaran = " << var[2] << std::endl;
    
    std::cout << "Luas persegi - lingkaran = ";
    std::cout << var[0] << " - " << var[2] << std::endl;
    std::cout << var[3];

    return 0;
}