#include <stdio.h>

int main(){
    int f, n;
    unsigned long long int fattoriale = 1;
    printf("\nDammi un numero di calcolero' il fattoriale: ");
    scanf("%d", &f);
    n = f; // facciamo un copia di f
    while (n > 0){
        fattoriale=fattoriale*n;
        n--;
    }
    printf("%d! e' uguale a %llu", f, fattoriale);
    return 0;
}