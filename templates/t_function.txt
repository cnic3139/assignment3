.text
.global <name>
.type <name>, @function
.p2align 4,,15

<name>:
	# save current frame pointer on stack
	pushq %rbp
	# set frame pointer
	movq  %rsp, %rbp
	# save callee-save registers that are used on stack
	pushq %rbx

	<allocate memory for local vector variables>

	<insert the body of function here>

	# epilogue of a function
	popq  %rbx # restore reg %rbx
	leave      # restore frame pointer
	ret        # return
