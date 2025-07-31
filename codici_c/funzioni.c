#include <stdio.h>

int somma(int a, int b){
    int som = a + b;
    return som;
}

int main(){
    int risultato;
    risultato = somma(5,7);
    printf("somma = %d", risultato);
}

