#include <iostream>

int main(){
    int i;
    printf("1. Bilangan genap 1 - 20\n\n> ");
    for (i = 0; i < 20; i++)
    {
        if (i%2 == 0) {
            std::cout << i << " ";
        } /*Optional*/ else {
            continue;
        }
    }

    int result = 0;
    printf("\n\n2. Bilangan ganjil 1 - 100\n\n> ");
    for (i = 0; i < 100; i++)
    {
        if (i%2 != 0) {
            result += i;
        } else {
            continue;
        }
    }
    std::cout << result << " ";

    printf("\n\n3. Star\n\n");
    int rows = 5;
    for(int i = 1; i <= rows; ++i) {
        for(int j = 1; j <= i; ++j) {
            std::cout << "* ";
        }
        std::cout << "\n";
    }
    
}