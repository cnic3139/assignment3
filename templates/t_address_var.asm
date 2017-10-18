# place address of <N>th local variable into <destreg>
movq  %rdi, <destreg>
imulq $4,   <destreg>, <destreg>
addq  $16,  <destreg>
imulq $<N>, <destreg>, <destreg>
subq  %rbp, <destreg>
negq  <destreg>
andq  $-16, <destreg>
