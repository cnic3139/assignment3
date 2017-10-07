	<load source address into %rax>
	<load destination address into %r10>

	movq   %rdi,   %rbx   # load vector length into counter %rbx
	shrq   $2,     %rbx   # divide counter reg by 4
	                      # (per loop iteration 4 floats) 
	jz     .loop_end<X>   # check whether number is equal to zero

.loop_begin<X>:           # loop header
	
	movaps (%rax), %xmm0  # load source into %xmm0
	movaps %xmm0,  (%r10) # store %xmm0

	# IMPORTANT: remove the following line only if %rax is
	# pointing to a constant
	addq   $16,    %rax   # increment source pointer by (4 x float)

	addq   $16,    %r10   # increment destination pointer by (4 x float)

	decq   %rbx           # decrement counter
	jnz    .loop_begin<X> # jump to loop header if counter is not zero

.loop_end<X>:
