#include <stdio.h>

#include <zlib.h>

int main(void) {
    printf("Hello, World!\n");
    printf("ZLIB VERSION: %s\n", zlibVersion());

    return 0;
}
