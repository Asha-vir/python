#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int size = 2 * n - 1;
    
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            // Find distance to the closest edge
            int min_i = i < size - i - 1 ? i : size - i - 1;
            int min_j = j < size - j - 1 ? j : size - j - 1;
            int min_dist = min_i < min_j ? min_i : min_j;
            
            // The value is n minus the distance from the outer edge
            printf("%d ", n - min_dist);
        }
        printf("\n");
    }
    
    return 0;
}
