#include <iostream>
#include <math.h>

using namespace std;

double lim(double x){
    //double y = (x-3)/(pow(x,2) - 2*x - 3);
    //double y = pow(x, 2)/(x-2);
    double y = (x-3)/(pow(x,2)-(2*x)-3);
    printf("%.17lf\n\n", y);
    return y;
}

int main(){
    double x;
    printf("Enter a number : ");
    cin >> x;
    lim(x);
    system("pause");
}