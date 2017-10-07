	<load source1 address into %rax>
	<load source2 address into %r10>
	<load destination address into %r11>

	movq   %rdi,   %rbx   # load vector length into counter %rbx
	shrq   $2,     %rbx   # divide counter reg by 4
	                      # (per loop iteration 4 floats)
	jz     .loop_end<X>   # check whether number is equal to zero

.loop_begin<X>:           # loop header

	movaps (%rax), %xmm0  # load first operand into %xmm0
	movaps (%r10), %xmm1  # load second operand into %xmm1

	# perform operation
	<operation> %xmm1, %xmm0

	movaps %xmm0,  (%r11) # store result

	# increment pointers

	# IMPORTANT: remove following line if %rax is pointing to a constant
	addq   $16,    %rax

	# IMPORTANT: remove followng line if %r10 is pointing to a constant
	addq   $16,    %r10

	addq   $16,    %r11

	decq   %rbx           # decrement counter
	jnz    .loop_begin<X> # jump to loop header if counter is not zero
.loop_end<X>:
