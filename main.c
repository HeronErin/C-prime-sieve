#include <stdio.h>
#include "root.c"
#include <stdlib.h>

typedef int itype;

struct Number{
    itype x;
    struct Number* next;
};

#define EXTENT 100
int main(){
    struct Number* numbers = (struct Number*) malloc(sizeof(struct Number) * EXTENT);

    // for ()



}