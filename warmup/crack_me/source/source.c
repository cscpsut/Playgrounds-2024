#include <stdio.h>
#include <string.h>

int main() {
    char username[20];
    char password[20];

    printf("Enter username: ");
    scanf("%s", username);

    printf("Enter password: ");
    scanf("%s", password);

    int correct = 1; 

    int hex_val0 = 0x4d;
    int hex_val1 = 0x6e;
    int hex_val2 = 0x7e;
    int hex_val3 = 0x7f;
    int hex_val4 = 0x7f;
    int hex_val5 = 0x40;
    int hex_val6 = 0x6c;
    int hex_val7 = 0x54;
    int hex_val8 = 0x40;
    int hex_val9 = 0x41;
    int hex_val10 = 0x45;
    int hex_val11 = 0x7a;
    int hex_val12 = 0x42;
    int hex_val13 = 0x52;
    int hex_val14 = 0x4a;
    int hex_val15 = 0x76;
    int hex_val16 = 0x4e;
    int hex_val17 = 0x5e;
    int hex_val18 = 0x4e;
    if ( (password[0] ^ hex_val0) != 0x1a ){ correct = 0; }
    if ( (password[12] ^ hex_val12) != 0x26 ){ correct = 0; }
    if ( (password[11] ^ hex_val11) != 0x25 ){ correct = 0; }
    if ( (password[14] ^ hex_val14) != 0x28 ){ correct = 0; }
    if ( (password[8] ^ hex_val8) != 0x22 ){ correct = 0; }
    if ( (password[17] ^ hex_val17) != 0x2b ){ correct = 0; }
    if ( (password[3] ^ hex_val3) != 0x1d ){ correct = 0; }
    if ( (password[9] ^ hex_val9) != 0x23 ){ correct = 0; }
    if ( (password[2] ^ hex_val2) != 0x1c ){ correct = 0; }
    if ( (password[18] ^ hex_val18) != 0x2c ){ correct = 0; }
    if ( (password[10] ^ hex_val10) != 0x24 ){ correct = 0; }
    if ( (password[4] ^ hex_val4) != 0x1e ){ correct = 0; }
    if ( (password[7] ^ hex_val7) != 0x21 ){ correct = 0; }
    if ( (password[1] ^ hex_val1) != 0x1b ){ correct = 0; }
    if ( (password[5] ^ hex_val5) != 0x1f ){ correct = 0; }
    if ( (password[16] ^ hex_val16) != 0x2a ){ correct = 0; }
    if ( (password[13] ^ hex_val13) != 0x27 ){ correct = 0; }
    if ( (password[6] ^ hex_val6) != 0x20 ){ correct = 0; }
    if ( (password[15] ^ hex_val15) != 0x29 ){ correct = 0; }
    
    if (strcmp(username, "admin") == 0 && correct) {
        printf("Well done!!\nwrap the password up with PlaygroundsCTF{} and submit it\n");
    } else {
        printf("Invalid username or password\n");
    }

    return 0;
}



