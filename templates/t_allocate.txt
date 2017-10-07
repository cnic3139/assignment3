# allocate <NUM> local variables
movq  %rdi,   %rax
imulq $4,     %rax, %rax
addq  $16,    %rax
imulq $<NUM>, %rax, %rax
subq  %rax,   %rsp
andq  $-16,   %rsp
