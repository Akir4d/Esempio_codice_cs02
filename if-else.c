#include <stdio.h>

int main()
{
    int numeratore;
    int denominatore;
    float divisione;

    printf("\nDammi in numeratore valore: ");
    scanf("%d", &numeratore);
    //printf("zona di memoria 0x%x contiene %d", &numeratore, numeratore);
    printf("\nDammi il denominatore valore: ");
    scanf("%d", &denominatore);

    if (denominatore !=0) {
        divisione = numeratore / denominatore;
        printf("\nil risultato di %d/%d=%f",numeratore, denominatore, divisione);
    } else {
        printf("\nmi spiace il denominatore non puo' essere 0");
    }

    return 0;
}