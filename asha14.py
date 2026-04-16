#include <stdio.h>

int main() {
    int n;
    int sum = 0;
    
    // Read the five-digit integer
    scanf("%d", &n);
    
    // Iterate until all digits are processed
    while (n > 0) {
        // Add the last digit to sum
        sum += (n % 10);
        
        // Remove the last digit from n
        n = n / 10;
    }
    
    printf("%d\n", sum);
    
    return 0;
}
