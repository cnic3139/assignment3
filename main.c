#include <stdlib.h>
#include <stdio.h>

/* alignment macro: aligns a memory block a to multiplies of a */
#define align(s,a) (((size_t)(s) + ((a) - 1)) & ~((size_t) (a) - 1))
/* Alignment for SSE unit */
#define SSE_ALIGN (16)
/* Number of elements */
#define NUM (100)

extern void mymin(long, float *, float *, float *);

int main(void) {
	float *a = malloc(sizeof(float) * NUM + SSE_ALIGN),
	      *b = malloc(sizeof(float) * NUM + SSE_ALIGN),
	      *c = malloc(sizeof(float) * NUM + SSE_ALIGN);
	/* Make sure that pointers are aligned to multiples of 16 bytes */
	a = (float *) align(a, SSE_ALIGN);
	b = (float *) align(b, SSE_ALIGN);
	c = (float *) align(c, SSE_ALIGN);

	/* Write values to a and b */
	for (int i = 0; i < NUM; i++) {
		a[i] = 1;
		b[i] = 2;
	}

	/* Invoke the function written in the vector language */
	mymin(NUM, a, b, c);

	/* Read values from c */
	for (int i = 0; i < NUM; i++) {
		printf("i: %d\n", i);
		printf("c[i]: %f\n", c[i]);
	}
	
	return 0;
}

