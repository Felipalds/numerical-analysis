#include <stdio.h>

int main(){

    double i = 0.11;
    double s = 0;

    printf("%f\n", i);

    for(int c = 0; c < 10000000; c++){
        s = i + s;
    }

    printf("%f\n", s);

    return 0;
}