	jmp .loopcond<NUM>

.loopbegin<NUM>:
	<emit code for loop-body here>

.loopcond<NUM>:
	<template for condition (.loopbegin<NUM>, .loopexit<NUM>)>

.loopend<NUM>:
