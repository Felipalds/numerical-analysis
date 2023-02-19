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
    int *pointsX = (int*)malloc(sizeof(int) * point_amount);
    int *pointsY = (int*)malloc(sizeof(int) * point_amount);

    for(int c = 0; c < point_amount; c++){
        int aux_int;
        printf("X%d: ", c);
        scanf("%d", &pointsX[c]);
        printf("Y%d: ", c);
        scanf("%d", &pointsY[c]);
    }

 
    if(point_amount)
    for(int c = 0; c < point_amount; c++){
        printf("(X: %d, Y: %d)", pointsX[c], pointsY[c]);
    }
    printf("\n");



}