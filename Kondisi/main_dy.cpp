#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    if (argc != 4)
    {
        printf("Usage: %s <integer> <integer> <operation>\n", argv[0]);
        return 1;
    }

    int *var = (int *)malloc(2 * sizeof(int));
    if (var == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }

    var[0] = atoi(argv[1]);
    var[1] = atoi(argv[2]);
    int opr = atoi(argv[3]);
    int result;

    switch (opr)
    {
        case 1:
            // Penjumlahan
            result = var[0] + var[1];
            printf("%d + %d = %d\n", var[0], var[1], result);
            break;
        case 2:
            // Pengurangan
            result = var[0] - var[1];
            printf("%d - %d = %d\n", var[0], var[1], result);
            break;
        case 3:
            // Perkalian
            result = var[0] * var[1];
            printf("%d * %d = %d\n", var[0], var[1], result);
            break;
        case 4:
            // Pembagian
            result = var[0] / var[1];
            printf("%d / %d = %d\n", var[0], var[1], result);
            break;
        default:
            printf("Error: Invalid operation.\n");
            free(var);
            return 1;
    }

    free(var);
    return 0;
}
