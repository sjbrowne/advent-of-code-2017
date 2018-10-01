
#include <stdio.h>
#include <stdint.h>

#define LIM 40000000

int bitmatch(uint64_t, uint64_t, uint16_t);

int main() {
    unsigned int tmin = 1<<31;
    int c = 0;
    uint64_t prev_a = 679, prev_b = 771;
    int fa = 16807, fb = 48271;
    uint16_t m = 65535;

    for (int i=0; i<LIM; i++) {
        prev_a = (fa*prev_a)%(tmin-1);   
        prev_b = (fb*prev_b)%(tmin-1);   
        if (bitmatch(prev_a, prev_b, m)) c++;
    }

    printf("part I:\n");
    printf("  16-bit matches: %d\n", c);
    return 0;
}

int bitmatch(uint64_t x, uint64_t y, uint16_t m) {
    return ((x & m)^(y & m)) == 0;  
}

