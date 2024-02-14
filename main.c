#include <stdio.h>

#include <stdlib.h>

// #define EXTENT 5000000
typedef int itype;
#define sqrt_f fast_sqrt_ui

#include "bulk.c"
#include "checker.c"
#include <time.h>

int main(){
    struct Number* buffer = makeNumberBuffer();
    
    clock_t t = clock();
    eleminateNonPrimes(buffer);

    double time_taken = ((double)(clock() - t))/CLOCKS_PER_SEC;
    printf("It took %f for %d numbers\n", time_taken, EXTENT);

    // bulkVerify(buffer);

    
}