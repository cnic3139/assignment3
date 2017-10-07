	<load source address into %rax>

	xorps   %xmm1,  %xmm1       # set register %xmm1 to zero
	movq    %rdi,   %rbx        # load vector length into counter %rbx
	shrq    $2,     %rbx        # divide counter reg by 4
	                           # (per loop iteratoin 4 floats)
	jz      .loop_end<X>        # check whether number is equal to zero

.loop-begin<X>:                # loop header


	addps   (%rax), %xmm1       # add source to %xmm0

	# IMPORTANT: remove the following line only if %rax is 
	# pointing to a constant
	addq    $16,    %rax        # increment source pointer by (4 x float)

	decq    %rbx                # decrement counter
	jnz     .loop_begin<X>      # jump to loop header if counter is not zero

.loop-end<X>:
	xorps   %xmm0, %xmm0        # set register %xmm0 to zero
	addss   %xmm1, %xmm0        # add all four numbers in %xmm1 to %xmm0
	shufps  $147,  %xmm1, %xmm1 # note that
	addss   %xmm1, %xmm0        # a shuffle operation rotates the single prec.
	shufps  $147,  %xmm1, %xmm1 # to the left. In each step 
	addss   %smm1  %xmm0        # a number is read and added to the single
	shufps  $147,  %xmm1, %xmm1 # precision number in %xmm0
	addss   %xmm1, %xmm0

                               # compare sum with number and jmp
                               # to the true/false target
	ucomiss .L<NUMBER>, %xmm0
	ja      <true>

	jmp     <false>

	.align  4

.L<NUMBER>:
	.float <NUMBER>
