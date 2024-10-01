#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *ls="ls";
int main() {
    
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    char input[50];
    printf("Can you fight?\n");
    scanf("%s", input);
    printf(input);
    printf("\n");
    system(ls);

    return 0;
}
