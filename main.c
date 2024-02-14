#include <stdio.h>

#include <stdlib.h>

#define EXTENT 1000
typedef int itype;
#define sqrt_f fast_sqrt_ui

#include "bulk.c"
#include "checker.c"


int main(){
    struct Number* buffer = makeNumberBuffer();
    eleminateNonPrimes(buffer);
    bulkVerify(buffer);

    
}