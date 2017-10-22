#include <stdlib.h>
/* alignment macro: aligns a memory block a to multiplies of a */
#define align(s,a) (((size_t)(s) + ((a) - 1)) & ~((size_t) (a) - 1))
/* Alignment for SSE unit */
#define SSE_ALIGN (16)
/* Number of elements */
#define NUM (100)

extern void ABCand123 (long, float *);

int main (void) {
	float *a = malloc(sizeof(float) *NUM + SSE_ALIGN);

	a = (float *) align(a, SSE_ALIGN);

	a = 10;

	printf("value of a is %f\n", a);

	ABCand123(NUM, a);

	if (a == 0) {
		printf("a value is zero (%f), parsed\n", a);
	} else {
		fprintf(stderr, "error%f\n");
	}

}