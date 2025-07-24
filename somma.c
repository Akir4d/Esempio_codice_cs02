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

    printf("\n%d + %d = %d", primo_numero, secondo_numero, risultato);
    printf("\n%d - %d = %d", primo_numero, secondo_numero, primo_numero - secondo_numero);
    printf("\n%d / %d = %.2f", primo_numero, secondo_numero, (float)primo_numero / (float)secondo_numero);
    printf("\n%d modulo %d = %d", primo_numero, secondo_numero, primo_numero % secondo_numero);
    secondo_numero++;
    primo_numero--;
    printf("\n%d + %d = %d", primo_numero, secondo_numero, risultato);
    printf("\n%d - %d = %d", primo_numero, secondo_numero, primo_numero - secondo_numero);
    printf("\n%d / %d = %.2f", primo_numero, secondo_numero, (float)primo_numero / (float)secondo_numero);
    printf("\n%d modulo %d = %d", primo_numero, secondo_numero, primo_numero % secondo_numero);
    return 0;
}