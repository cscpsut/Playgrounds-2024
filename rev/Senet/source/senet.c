#include <stdio.h>
#include <string.h>
#include <openssl/sha.h> 
#include <stdlib.h>

void setup() {
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}


#define ROWS 10
#define COLS 3

void printBoard(char board[ROWS][COLS], int playerRow, int playerCol) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (i == playerRow && j == playerCol) {
                printf("P ");
            } else {
                printf("%c ", board[i][j]);
            }
        }
        printf("\n");
    }
}

void sha1_hash(const unsigned char *data, size_t length, unsigned char hash[SHA_DIGEST_LENGTH]) {
    SHA1(data, length, hash);
}

void print_hash(unsigned char hash[SHA_DIGEST_LENGTH], char output[41]) {
    for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
        sprintf(output + (i * 2), "%02x", hash[i]);
    }
    output[40] = '\0';  
}

int main() {
    setup();
    char board[ROWS][COLS];
    memset(board, '.', sizeof(board));  

    int playerRow = 0;
    int playerCol = COLS / 2;  
    char moves[9]; 
    int moveCount = 0;

    printf("Welcome to my version of Senet!\n");
    printBoard(board, playerRow, playerCol);

    while (playerRow < ROWS - 1 && moveCount < 9) {
        if (playerCol == 0) {
            printf("Choose your move (R: Right, F: Forward): ");
        } else if (playerCol == 2) {
            printf("Choose your move (L: Left, F: Forward): ");
        } else {
            printf("Choose your move (L: Left, R: Right, F: Forward): ");
        }

        char move;
        scanf(" %c", &move);
        
        if (move == 'L') {
            if (playerCol > 0) {
                playerCol--;
            } else {
                printf("Invalid move! Try again.\n");
                continue;
            }
        } else if (move == 'R') {
            if (playerCol < COLS - 1) {
                playerCol++;
            } else {
                printf("Invalid move! Try again.\n");
                continue;
            }  
        } else if (move != 'F') {
            printf("Invalid move! Try again.\n");
            continue;
        }
        
        playerRow++;
        moves[moveCount++] = move;
        printBoard(board, playerRow, playerCol);
    }

    unsigned char hash[SHA_DIGEST_LENGTH];
    sha1_hash((unsigned char *)moves, moveCount, hash);

    char hash_output[41];
    print_hash(hash, hash_output);

    char target_hash[] = "5366dcb274410ad1613ee90d3b568af34b3ba90e";

    if (strcmp(hash_output, target_hash) == 0) { 
        printf("Yay, you win!\n"); 
        // printf("Connect to the instance to get your flag <3");
        printf(getenv("FLAG"));
    } else { 
        printf("lol, you lose!\n"); 
    }

    return 0;
}