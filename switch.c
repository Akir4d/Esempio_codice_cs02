#include <stdio.h>

int main()
{
    char scelta;
    printf("\nPremi 'a' per  menu' a");
    printf("\nPremi 'b' per  menu' b");
    printf("\nPremi 'c' per  menu' c");
    printf("\nscelta: ");
    scanf("%c", &scelta);
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
    default:
        printf("\nMi spiace non ho capito");
        break;
    }
    return 0;
}