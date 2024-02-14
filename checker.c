#pragma once
#include <stdbool.h>
#include "bulk.c"


// Slow, but 100% accurate
bool isPrime(itype x){
    itype eleminationLimit = sqrt_f(EXTENT)+1;

    // Edge cases
    if (x <= 3) return true;
    if (x <= eleminationLimit) eleminationLimit=x-2;;

    for (itype divisor = 2; divisor <= eleminationLimit; divisor++){
        if (x % divisor == 0) return false;
    }
    return true;
}

void bulkVerify(struct Number* itr){
    while (itr){
        printf("%i - %x\n", itr->x, isPrime(itr->x));
        itr = itr->next;
    }
}