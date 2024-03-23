#include <stdio.h>

int main() {
    FILE* in = fopen("out.bin", "rb");
    char c;
    #define X 25135
    double dest[(X / sizeof(double)) + 1];
    fread(dest, 1, X, in);
    return 0;
}