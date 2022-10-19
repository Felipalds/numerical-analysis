#include <stdio.h>
#include <math.h>


int main(){

    double x, h;
    double p = 0.1;

    printf("Function: f(x) = sen(x^2) \n");

    printf("NUMBER: \n");
    scanf("%lf", &x);
    printf("PRECISION: \n");
    scanf("%lf", &h);

    

    for(int c = 1; c <= 100; c++){
        p = p / c * 10;
        double derivate = (sin( pow(x + p, 2) ) - sin ( pow(x , 2) ) ) / p;
        printf("DERIVATE: %f\n", derivate);
        if(derivate == 0){
            break;
        }
    }

    printf("LAST PRECISION: %f", p);



    return 0;
}