#include <stdlib.h>
#include <stdio.h>
/* alignment macro: aligns a memory block a to multiplies of a */
#define align(s,a) (((size_t)(s) + ((a) - 1)) & ~((size_t) (a) - 1))
/* Alignment for SSE unit */
#define SSE_ALIGN (16)
/* Number of elements */
#define NUM (100)

extern void trivial (long, float *);

int main (void) {
	float *a = malloc(sizeof(float) *NUM + SSE_ALIGN);

	a = (float *) align(a, SSE_ALIGN);

	for (int i = 0; i < NUM; i++) {
		a[i] = 10;
	}

	trivial(NUM, a);
	for (int i = 0; i < NUM; i++) {
		printf("value of a is %f\n", a[i]);
	}
}