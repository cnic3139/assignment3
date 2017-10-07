grammar VPL;

M : F M
  | /* epsilon */
  ;

F : func ident P D S end
  ;

P : '(' L ')'
  ;

L : ident
  | ident ',' L
  ;

D : var L ';'
  | /* epsilon */
  ;

S : if C then S endif
  | while C do S endwhile
  | S ';' S
  | ident '=' E
  | /* epsilon */
  ;

E : add '(' E ',' E ')'
  | minus '(' E ',' E ')'
  | mult '(' E ',' E ')'
  | div '(' E ',' E ')'
  | min '(' E ',' E ')'
  | '(' E ')'
  | ident
  | num
  ;

C : E '<' num
  | E '>' num
  ;

ident : [a-zA-Z_][a-zA-Z0-9_]*
      ;

num : [0-9]+(\.[0-9]+)?
    ;