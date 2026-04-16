#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[1001];
    int frequency[10] = {0}; // Initialize all 10 counts to 0

    // Read the string from stdin
    scanf("%s", s);

    // Iterate through the string
    for (int i = 0; s[i] != '\0'; i++) {
        // Check if the character is a digit
        if (isdigit(s[i])) {
            // Convert char to int index (e.g., '1' - '0' = 1)
            frequency[s[i] - '0']++;
        }
    }

    // Print the results separated by spaces
    for (int i = 0; i < 10; i++) {
        printf("%d ", frequency[i]);
    }

    return 0;
}
