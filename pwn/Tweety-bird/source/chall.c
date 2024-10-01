#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void setup(){

    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

}

void banner(){
    printf("\033[38;2;255;255;0m");
    printf("          ___\n");
    printf("      _.-'   ```'--.._\n");
    printf("    .'                `-._\n");
    printf("   /                      `.\n");
    printf("  /                         `.\n");
    printf(" /                            `.\n");
    printf(":       (                       \\\n");
    printf("|    (   \\_                  )   `.\n");
    printf("|     \\__/ '.               /  )  ;\n");
    printf("|   (___:    \\            _/__/   ;\n");
    printf(":       | _  ;          .'   |__) :\n");
    printf(" :      |` \\ |         /     /   /\n");
    printf("  \\     |_  ;|        /`\\   /   /\n");
    printf("   \\    ; ) :|       ;_  ; /   /\n");
    printf("    \\_  .-''-.       | ) :/   /\n");
    printf("   .-         `      .--.'   /\n");
    printf("  :         _.----._     `  <\n");
    printf("  :       -'........'-       `.\n");
    printf("   `.        `''''`           ;\n");
    printf("     `'-.__                  ,'\n");
    printf("           ``--.   :'-------'\n");
    printf("               :   :\n");
    printf("              .'   '.\n");
    printf("\033[0m");
}



void gadgets(){ 
__asm__( "pop %rdi;" 
        "ret;"  );
}

void vuln() {
    setup();
    banner();

    char buffer[64];

    puts("I tawt I taw a puddy tat!");
    gets(buffer);
    printf(buffer);

    memset(buffer,'\0',63);

    puts("\nSufferin' Succotash");
    gets(buffer);
}

int main() {
    vuln();
}