#include <stdio.h>

int main()
{
    int primo_numero;
    int secondo_numero;
    int risultato;

    printf("\nDammi in primo valore: ");
    scanf("%d", &primo_numero);
    //printf("zona di memoria 0x%x contiene %d", &primo_numero, primo_numero);
    printf("\nDammi il secondo valore: ");
    scanf("%d", &secondo_numero);

    risultato = primo_numero + secondo_numero;
    printf("la somma di %d + %d = %d", primo_numero, secondo_numero, risultato);

    return 0;
}