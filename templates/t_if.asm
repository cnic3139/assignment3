	# Template for conditional(.true-branch<NUM>, .false-branch<NUM>)
	<template>

.true-branch<NUM>:
	
	# Emit code for true-branch here
	<true-branch>

	jmp .endif<NUM>

.false-branch<NUM>:

.endif<NUM>:
