#include <stdio.h>
#include <stdlib.h>

int main(){
    int point_amount = 0;
    
    printf("INTEGRAÇÃO NUMÉRICA\n");
    printf("Quantos pontos você possui?\n");
    scanf("%d", &point_amount);
    while(point_amount < 1){
        printf("Impossível realizar integração.");
    }
    float *pointsX = (float*)malloc(sizeof(float) * point_amount);
    float *pointsY = (float*)malloc(sizeof(float) * point_amount);
    float integral = 0;

    for(int c = 0; c < point_amount; c++){
        int aux_int;
        printf("X%d: ", c);
        scanf("%f", &pointsX[c]);
        printf("Y%d: ", c);
        scanf("%f", &pointsY[c]);
    }

    for(int c = point_amount - 1; c > 0; c--){
        float x1 = pointsX[c];
        float x0 = pointsX[c - 1];
        float h = x1 - x0;
        float y1 = pointsY[c];
        float y0 = pointsY[c - 1];
        float y = y1 + y0;
        integral += (h/2)*(y);
    }
    
    for(int c = 0; c < point_amount; c++){
        printf("(X: %f, Y: %f)", pointsX[c], pointsY[c]);
    }
    printf("\n Integral is: %f \n", integral);

    return 0;

}