#include <iostream>
#include <random>
#include <chrono>
#include <thread>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    // // Memulai mengukur waktu
    // auto start_time = std::chrono::high_resolution_clock::now();

    // 10 Bilangan

    int val = std::stoi(argv[1]);
    float sum = 0;
    int arr[val];

    srand(static_cast<unsigned>(time(nullptr)));
    int ub = std::stoi(argv[2]), lb = std::stoi(argv[3]);

    for (auto i = 0; i < val; i++){
        arr[i] = (rand() % lb) + ub;
        std::cout << "Enter value[" << i << "] :" << arr[i];

        // std::this_thread::sleep_for(std::chrono::milliseconds(500));
        
        std::cout << "\r";
        // std::cin >> arr[i];
    }
    std::cout << std::endl;


    printf("\nReversed : ");
    for (auto i = val-1; i >= 0; i--){
        std::cout << arr[i] << " ";
        sum = sum + arr[i];
    }
    
    printf("\nOdd : ");
    int even, odd; 
    for (auto i = 0; i < val; i++){
        if (arr[i]%2 != 0)
        {
            std::cout << arr[i] << " ";
            odd++;
        } else {
            even++;
        }
    }

    std::cout << "\nOdd Cound = " << odd << "\n";
    std::cout << "Even Cound  = " << even << "\n";
    
    std::cout << "Average : " << sum/(sizeof(arr)/sizeof(arr[0])) << "\n\n";

    // // Mengakhiri mengukur waktu
    // auto end_time = std::chrono::high_resolution_clock::now();

    // // Menghitung waktu yang telah berlalu dalam milidetik
    // auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    // std::cout << "Waktu eksekusi: " << elapsed_time << " ms" << std::endl;
    
    // system("pause");
    return 0;
}


/*
#include <iostream>
#include <chrono>

int main() {

    // Panggil fungsi main atau kode utama programmu di sini
    // Misalnya, main();

    return 0;
}

*/