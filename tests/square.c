#include <stdlib.h>
/* alignment macro: aligns a memory block a to multiplies of a */
#define align(s,a) (((size_t)(s) + ((a) - 1)) & ~((size_t) (a) - 1))
/* Alignment for SSE unit */
#define SSE_ALIGN (16)
/* Number of elements */
#define NUM (100)

extern void square (long, float *, float *);

int main (void) {
	float *a = malloc(sizeof(float) *NUM + SSE_ALIGN);
	float *a = malloc(sizeof(float) *NUM + SSE_ALIGN);

	a = (float *) align(a, SSE_ALIGN);
	c = (float *) align(c, SSE_ALIGN);

	a = 7;

	printf("value of a is %f\n", a);

	square(NUM, a, c);

	if (c == a*a) {
		printf("c value is %f and is square of a\n", c);
	} else {
		fprintf(stderr, "c value is %f and not square of a\n", c);
	}

}