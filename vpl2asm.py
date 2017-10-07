#!/usr/bin/env python3
import sys
import antlr3
from build.VPLLexer import VPLLexer
from build.VPLParser import VPLParser

char_stream = antlr3.ANTLRInputStram(sys.stdin)
lexer = VPLLexer(char_stream)
tokens = antlr3.CommonTokenStream(Lexer)
parser = VPLParse(tokens)
root = parser.prog()

