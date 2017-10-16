grammar VPL;

start: m;

m : f m
  | /* epsilon */
  ;

f : 'func' IDENT p d s 'end'
  ;

p : '(' l ')'
  ;

l : IDENT
  | IDENT ',' l
  ;

d : 'var' l ';'
  | /* epsilon */
  ;

s : 'if' c 'then' s 'endif' r
  | 'while' c 'do' s 'endwhile' r
  | IDENT '=' e r
  | r
  ;

r : ';' s
  | /* epsilon */
  ;

e : 'add' '(' e ',' e ')'
  | 'minus' '(' e ',' e ')'
  | 'mult' '(' e ',' e ')'
  | 'div' '(' e ',' e ')'
  | 'min' '(' e ',' e ')'
  | '(' e ')'
  | IDENT
  | NUM
  ;

c : e '<' NUM
  | e '>' NUM
  ;

IDENT : ( 'a'..'z' | 'A'..'Z' | ' _' )( 'a'..'z' | 'A'..'Z' | '0'..'9' | '_' )*
  ;

NUM : ( '0'..'9' )+ ('.'( '0'..'9' )+)?;

UNICODE_WS : [\p{White_Space}] -> skip; // match all Unicode whitespace
