#include <stdio.h>
#include <stdlib.h> // Required for the abs() function

void update(int *a, int *b) {
    // 1. Store the original values using dereferencing (*)
    int original_a = *a;
    int original_b = *b;

    // 2. Update the value at address 'a' with the sum
    *a = original_a + original_b;

    // 3. Update the value at address 'b' with the absolute difference
    // abs() returns the non-negative value of the result
    *b = abs(original_a - original_b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
