#include <iostream>
#include <string>

int main(int argc, char **argv)
{
    if (argc != 4)
    {
        printf("Usage: %s <integer> <operation> <integer>\n", argv[0]);
        return 1;
    }

    int var[2] = {std::stoi(argv[1]), std::stoi(argv[3])};
    std::string opr = argv[2];  // Menggunakan std::string untuk operator

    int result;
    if (opr == "+")
    {
        // Penjumlahan
        result = var[0] + var[1];
        printf("%d + %d = %d\n", var[0], var[1], result);
    }
    else if (opr == "-")
    {
        // Pengurangan
        result = var[0] - var[1];
        printf("%d - %d = %d\n", var[0], var[1], result);
    }
    else if (opr == "*")
    {
        // Perkalian
        result = var[0] * var[1];
        printf("%d * %d = %d\n", var[0], var[1], result);
    }
    else if (opr == "/")
    {
        // Pembagian
        result = var[0] / var[1];
        printf("%d / %d = %d\n", var[0], var[1], result);
    }
    else
    {
        printf("Error: Invalid operator.\n");
        return 1;
    }

    return 0;
}
