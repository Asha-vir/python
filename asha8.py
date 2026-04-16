#include <stdio.h>

int main() 
{
    char ch;
    char s[100];
    char sen[100];

    // 1. Read a single character
    scanf("%c", &ch);
    
    // 2. Read a single word (until space or newline)
    scanf("%s", s);
    
    // 3. Consume the leftover newline from the previous entry 
    // and read the entire remaining sentence until the next newline
    scanf("\n%[^\n]%*c", sen);
    
    // Print the results
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);

    return 0;
}
