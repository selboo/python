#include <stdio.h>

int add_number(int n) 
{ 
    static int i=100; 
    i+=n; 
    return i; 
}

int main() {
    int k = add_number(100);
    k+=add_number(100);
    printf("%d", k);
    return 0;
}
