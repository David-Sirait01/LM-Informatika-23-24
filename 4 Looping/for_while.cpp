#include <iostream>

using namespace std;


int main(){
    int i = 0;
    // For
    printf("\n\n[for] \n");
    cout << "i which at " << &i << " has allocated\n\n";
    for(i = 0; i < 5; i++){
        cout << "Iterasi ke " << i << endl;
    }
    
    printf("\n\n[While]\n");
    // While
    i = 0;
    while (i < 5)
    {
        cout << "Iterasi ke " << i << endl;
        i++;
    }

    i = 0;
    printf("\n\n[Do-While]\n");
    do
    {
        cout << "Iterasi ke " << i << endl;
        i++;
    } while (i<5);
    

    printf("\n");system("pause");
}