#include <stdio.h>

int main()
{
    int primo;
    int secondo;

    printf("\nDammi in primo valore: ");
    scanf("%d", &primo);
    //printf("zona di memoria 0x%x contiene %d", &primo, primo);
    printf("\nDammi il secondo valore: ");
    scanf("%d", &secondo);

    if (primo == secondo) printf("\n%d e %d sono uguali", primo, secondo);
    if (primo != secondo) printf("\n%d e %d non sono uguali", primo, secondo);
    if (primo < secondo) printf("\n%d e' inferiore a %d", primo, secondo);
    if (primo > secondo) printf("\n%d e' maggiore di %d", primo, secondo);
    if (primo <= secondo) printf("\n%d e' inferiore o uguale a %d", primo, secondo);
    if (primo >= secondo) printf("\n%d e' maggiore o uguale a %d", primo, secondo);
    if ((primo % 2 == 0) && (secondo % 2 == 0)) printf("\nsia %d che %d sono pari", primo, secondo);
    if ((primo % 2 == 0) || (secondo % 2 == 0)) printf("\nfra %d e %d c'e' un numero pari", primo, secondo);
    if (!(primo % 2 == 0)) printf("\n%d e' dispari", primo);
    return 0;
}