	<template for condition(.true-branch<NUM>, .false-branch<NUM>)>

.true-branch<NUM>:

	<emit code for true-branch here>

	jmp .endif<NUM>

.false-branch<NUM>:

.endif<NUM>:
