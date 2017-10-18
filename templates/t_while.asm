	jmp .loopcond<NUM>

.loopbegin<NUM>:
	# Emit code for loop-body here
	<loop-body>

.loopcond<NUM>:
	# Emit code for condition (.loopbegin<NUM>, .loopexit<NUM>)
	<template>

.loopend<NUM>:
