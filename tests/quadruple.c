#include <stdlib.h>
/* alignment macro: aligns a memory block a to multiplies of a */
#define align(s,a) (((size_t)(s) + ((a) - 1)) & ~((size_t) (a) - 1))
/* Alignment for SSE unit */
#define SSE_ALIGN (16)
/* Number of elements */
#define NUM (100)

extern void quadruple (long, float *, float *);

int main (void) {
	float *a = malloc(sizeof(float) *NUM + SSE_ALIGN);
	float *b = malloc(sizeof(float) *NUM + SSE_ALIGN);

	a = (float *) align(a, SSE_ALIGN);
	b = (float *) align(b, SSE_ALIGN);

	a = 4;

	printf("value of a is %f\n", a);

	quadruple(NUM, a, b);

	if (b == a * 4) {
		printf("b value is %f and is 4 times of a\n", b);
	} else {
		fprintf(stderr, "b value is %f and not 4 times of a\n", b);
	}

}