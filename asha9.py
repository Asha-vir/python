#include <stdio.h>

int main()
{
    int n, m;
    float x, y;

    // Read two integers from the first line
    scanf("%d %d", &n, &m);
    
    // Read two floats from the second line
    scanf("%f %f", &x, &y);

    // Print integer sum and difference
    printf("%d %d\n", n + m, n - m);
    
    // Print float sum and difference rounded to 1 decimal place
    // %.1f ensures only one digit after the decimal point is shown
    printf("%.1f %.1f\n", x + y, x - y);

    return 0;
}
