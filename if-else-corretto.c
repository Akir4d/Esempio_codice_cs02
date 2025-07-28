#include <stdio.h>

int main()
{
    float numeratore;
    float denominatore;
    float divisione;
    printf("\naccetto anche valori in virgola mobile con notazione inglese (1.2 etc)");
    printf("\nDammi in numeratore valore: ");
    scanf("%f", &numeratore);
    //printf("zona di memoria 0x%x contiene %d", &numeratore, numeratore);
    printf("\nDammi il denominatore valore: ");
    scanf("%f", &denominatore);

    if (denominatore !=0) {
        divisione = numeratore / denominatore;
        printf("\nil risultato di %.2f/%.2f=%.4f",numeratore, denominatore, divisione);
    } else {
        printf("\nmi spiace il denominatore non puo' essere 0");
    }

    return 0;
}