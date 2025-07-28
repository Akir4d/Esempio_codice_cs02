#include  <stdio.h>

void scrivivettore(int *ptr){
    for(int i=0; i<10; i++){
        printf("\nInserisci valore per 0x%x: ", ptr);
        scanf("%d", ptr);
        ptr++;
    }
}

void leggivettore (int *ptr){
    for (int i =0; i < 10; i++)
    {
        printf("\nn[%d]=0x%x=%d", i, ptr, *ptr);
        ptr++;
    }
}

int main(){
    int n[10] = {0};
    int *n_ptr;

    n_ptr = &n[0];

    scrivivettore(n_ptr);
    leggivettore(n_ptr);
}