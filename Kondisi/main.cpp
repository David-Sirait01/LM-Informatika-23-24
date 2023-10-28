#include <iostream>
#include <vector>

/*
int main(){

    if (var%2 == 0)
    {
        printf("%d is even", var);
    } else {
        printf("%d is odd", var);
    }
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    int a;
    printf("Enter a value : ");
    scanf("%i", &a);

    std::vector<int> num[1];
    char opr;
    printf("Enter 1st number")
    std::cin >> num[1];
    printf("Enter 2nd number")
    std::cin >> num[2];

    printf("Enter oeprator")
    std::cin >> opr;
}
*/

int main(int argc, char **argv)
{
    if (argc != 4)
    {
        printf("Usage: %s <integer> <integer> <integer>\n", argv[0]);
        printf("operators <int>\n1 Additionn\n2 Substract\n3 Multiplication\n4 Sivision");
        printf("\n\nexample : .\\main 2 2 1 -> 4");
        return 1;
    }

    int var[2] = {std::stoi(argv[1]), std::stoi(argv[2])};
    

    int opr = std::stoi(argv[3]);
    int result;
    switch (opr)
    {
        case 1:
            // Penjumlahan
            result = var[0] + var[1];
            printf("%d + %d = %d", var[0], var[1], result);
            break;  
        case 2:
            // Pengurangan
            result = var[0] - var[1];
            printf("%d - %d = %d", var[0], var[1], result);
            break;
        case 3:
            // Perkalian
            result = var[0] * var[1];
            printf("%d * %d = %d", var[0], var[1], result);
            break;
        case 4:
            // Pembagian
            result = var[0] / var[1];
            printf("%d / %d = %d", var[0], var[1], result);
            break;

    default:
        printf("Error : out of index");
        break;
    }    

    system("pause");
    return 0;
}
