#include <stdlib.h>
/* alignment macro: aligns a memory block a to multiplies of a */
#define align(s,a) (((size_t)(s) + ((a) - 1)) & ~((size_t) (a) - 1))
/* Alignment for SSE unit */
#define SSE_ALIGN (16)
/* Number of elements */
#define NUM (100)

extern void simple (long, float *, float *, float *);
extern void addinadd (long, float *, float *, float*, float*);
extern void clone (long, float *, float *);

int main (void) {
	float *a = malloc(sizeof(float) *NUM + SSE_ALIGN);
	float *b = malloc(sizeof(float) *NUM + SSE_ALIGN);
	float *c = malloc(sizeof(float) *NUM + SSE_ALIGN);

	a = (float *) align(a, SSE_ALIGN);
	b = (float *) align(b, SSE_ALIGN);
	c = (float *) align(c, SSE_ALIGN);
	

	a = 17;
	b = 5;

	biggerorsmaller(NUM, a, b, c);

	if (c == 12) {
		printf("values of a, b and c are %f, %f and %f\n", a, b, c);
	} else {
		fprintf(stderr, "c is %f, should be 12\n", c);
	}

	a = 1.1;
	b = 2.2;
	c = 3.3;

	addinadd(NUM, a, b, c, d);

	if (d == a + b + b + c) {
		printf("d value is %f\n", d);
	} else {
		fprintf(stderr, "d value is %f and is wrong, should be %f\n", c, a + b + b + c);
	}

	a = 42;

	clone(NUM, a, b);

	if (b == a) {
		printf("b value is %f and is same of a\n", b);
	} else {
		fprintf(stderr, "c value is %f and not same of a\n", b);
	}


}