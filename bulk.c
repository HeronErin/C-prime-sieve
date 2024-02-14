#pragma once
#include "root.c"

// Insanly fast prime gen.


struct Number{
    itype x;
    struct Number* next;
};
void printNumbers(struct Number* itr){
    printf("---------------\n");
    while (itr){
        printf("%i\n", itr->x);
        itr=itr->next;
    }
    printf("---------------\n");
}

struct Number* makeNumberBuffer(){
    // Get the memory
    struct Number* numbers = (struct Number*) malloc(sizeof(struct Number) * EXTENT);
    
    // Fill the linked list:
    numbers->x = 2;
    for (itype x = 3; x < EXTENT+1; x++){
        numbers[x-2].x = x;
        numbers[x-3].next = &numbers[x-2];
    }
    numbers[EXTENT-2].next = 0;
    
    return numbers;
} 


void _primeEliminationStage(struct Number* itr){
    itype divisor = itr->x;
    struct Number* last_possible_prime = itr;

    itr=itr->next;
    while(itr){
        if (itr->x % divisor == 0)
            last_possible_prime->next = itr->next;
        else
            last_possible_prime = itr;
        
        itr = itr->next;
    }
}
void eleminateNonPrimes(struct Number* list){
    itype eleminationLimit = sqrt_f(EXTENT)+1;
    while (list && list->x <= eleminationLimit){
        _primeEliminationStage(list);
        list = list->next;
    }
}
