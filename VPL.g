grammar VPL;

start: m;

m : f m
  | /* epsilon */
  ;

f : 'func' ident p d s 'end'
  ;

p : '(' l ')'
  ;

l : ident
  | ident ',' l
  ;

d : 'var' l ';'
  | /* epsilon */
  ;

s : 'if' c 'then' s 'endif' r
  | 'while' c 'do' s 'endwhile' r
  | ident '=' e r
  | /* epsilon */
  ;

r : ';' s r
  | /* epsilon */
  ;

e : 'add' '(' e ',' e ')'
  | 'minus' '(' e ',' e ')'
  | 'mult' '(' e ',' e ')'
  | 'div' '(' e ',' e ')'
  | 'min' '(' e ',' e ')'
  | '(' e ')'
  | ident
  | num
  ;

c : e '<' num
  | e '>=' num
  ;

ident : IDENT;

num : NUM;

IDENT : ( 'a'..'z' | 'A'..'Z' | ' _' )( 'a'..'z' | 'A'..'Z' | '0'..'9' | '_' )*;

NUM : ( '0'..'9' )+ ('.'( '0'..'9' )+)?;

UNICODE_WS : [\p{White_Space}] -> skip; // match all Unicode whitespace
