#include <stdio.h>

int main()
{
    char scelta;
    do
    {
        printf("\nPremi 'a' per  menu' a");
        printf("\nPremi 'b' per  menu' b");
        printf("\nPremi 'c' per  menu' c");
        printf("\nscelta (premi u per uscire): ");
        scanf(" %c", &scelta); // lo spazio serve nel char per evitare la cattura di \r e \n
        switch (scelta)
        {
        case 'A':
            // printf("\nEcco il menu' A");
        case 'a':
            printf("\nEcco il menu' A");
            break;
        case 'B':
        case 'b':
            printf("\nEcco il menu' B");
            break;
        case 'C':
        case 'c':
            printf("\nEcco il menu' C");
            break;
        case 'u':
            printf("\nGrazie per averci scelto!");
            break;
        default:
            printf("\nMi spiace non ho capito");
            break;
        }
    }  while (scelta != 'u');
    return 0;
}