#include <stdio.h>
#include <stdlib.h>

int main(){

    char choice;
    printf("Simpson! \n");
    printf("a. Simples;  b. Composto \n");
    scanf("%c", &choice);
    float integral;

    if(choice == 'a'){
        float *pointsX = (float*)malloc(sizeof(float) * 3);
        float *pointsY = (float*)malloc(sizeof(float) * 3);

        for(int c = 1; c <= 3; c++){
            printf("X[%d]: ", c);
            scanf("%f", &pointsX[c-1]);
            printf("Y[%d]: ", c);
            scanf("%f", &pointsY[c-1]);
        }
        float h = (pointsX[1] - pointsX[0]);
        integral = h/3*(pointsY[0] + 4*pointsY[1] + pointsY[2]);
    }
    if(choice == 'b'){
        float *pointsX = (float*)malloc(sizeof(float) * 5);
        float *pointsY = (float*)malloc(sizeof(float) * 5);

        for(int c = 1; c <= 5; c++){
            printf("X[%d]: ", c);
            scanf("%f", &pointsX[c-1]);
            printf("Y[%d]: ", c);
            scanf("%f", &pointsY[c-1]);
        }
        float h = (pointsX[1] - pointsX[0]);
        integral = h/3*(pointsY[0] + 4*pointsY[1] + 2*pointsY[2] + 4*pointsY[3] + pointsY[4]);
    }
    printf("Integral is: %f \n", integral);
    return 0;
}