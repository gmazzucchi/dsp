#include <stdio.h>
#include <stdint.h>
#include <math.h>

#define PI 3.14159265358979323846
#define TAU (2.0 * PI)

int main() {
    int16_t signal[46876];
    int nsamples = sizeof(signal) / sizeof(signal[0]);

    int i = 0;
    while(i < nsamples) {
        double t = ((double)i/2.0)/((double)nsamples);
        signal[i] = 32767*sin(100.0 * TAU * t); // left
        signal[i+1] = signal[i]; // right
        i += 2;
    }
    for (size_t i = 0; i < 46876; i++) {
        printf("%d ", (int) signal[i]);
    }
    printf("\n");
    
    return 0;
}
    