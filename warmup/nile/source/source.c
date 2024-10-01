#include <stdio.h>
#include <stdlib.h>

void setup() {
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main() {

    setup();

    int userNumber;
    int num = 2144444444 ;
    int favorite_number = -42000000;

    char flag[100];
    FILE *flagFile = fopen("flag.txt", "r");
    if (flagFile == NULL) {
        perror("Error opening flag file");
        return 1;
    }
    if (fgets(flag, sizeof(flag), flagFile) == NULL) {
        perror("Error reading flag file");
        fclose(flagFile);
        return 1;
    }
    fclose(flagFile);




    printf("Enter a number: ");
    while (scanf("%d", &userNumber) != 1) {
        printf("Invalid input! Please enter a number: ");
        while (getchar() != '\n'); // Clear input buffer
    }

    if (userNumber < 0) {
        printf("Please enter a positive number.\n");
        return 1;
    }

    int result = userNumber + num;
    printf("The result is: %d\n", result);
    
    if (result == favorite_number) {

        printf("Congratulations! You win! The flag is: %s\n", flag);

    } else {
        printf("Sorry, you didn't get my favorite number. Try again!\n");
        printf("Psst... It's %d.\n", favorite_number);
    }

    return 0;
}
