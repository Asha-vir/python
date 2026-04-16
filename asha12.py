#include <stdio.h>

int main() 
{
    char s[100];
    
    // Read the full line of input until a newline is encountered
    // %[^\n] tells scanf to read everything except the newline character
    scanf("%[^\n]%*c", s);
    
    // Print the static "Hello, World!" followed by a newline
    printf("Hello, World!\n");
    
    // Print the input string 's'
    printf("%s", s);

    return 0;
}
