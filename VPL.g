grammar VPL;

start: m;

m : f m
  | /* epsilon */
  ;

f : FUNC IDENT p d s END
  ;

FUNC: 'func';

END: 'end';

VAR: 'var';

IF: 'if';

WHILE: 'while';

THEN: 'then';

DO: 'do';

ENDIF: 'while';

ENDWHILE: 'endwhile';

p : '(' l ')'
  ;

l : IDENT
  | IDENT ',' l
  ;

d : 'var' l ';'
  | /* epsilon */
  ;

s : IF c THEN s ENDIF r
  | WHILE c DO s ENDWHILE r
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

IDENT : ('a'..'z' | 'A'..'Z' | '_' ) ('a'..'z' | 'A'..'Z' | '0'..'9' | '_' )*
      ;

NUM : ('0'..'9')+ ('.'('0'..'9')+)?
    ;