#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void check_access() {
    FILE *file;
    char file_content[256];

    file = fopen("egypt.txt", "r");
    if (file == NULL) {
        printf("Failed to open egypt.txt\n");
        return;
    }

    if (fgets(file_content, sizeof(file_content), file) != NULL) {
        if (strstr(file_content, "egyptmotherworld") != NULL) {
            printf("PlaygroundsCTF{D0Ra_TH3_3XP10R3R_1N_3GYPT}\n");
        } else {
            printf("Access denied!\n");
        }
    } else {
        printf("Failed to read from file\n");
    }

    fclose(file);
}


void gadgets() {
    asm volatile("ret");                  
    asm volatile("pop %rax; ret");        
    asm volatile("syscall; ret");              
}

int main() {
    
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    char input[50];

    printf("Hi, I'm Dora! Can you see a flag? I can't find it.\n");
    gets(input); 

    check_access();
    return 0;
}
