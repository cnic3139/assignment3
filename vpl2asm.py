#!/usr/bin/env python3
import sys
from antlr4 import *
from build.VPLLexer import VPLLexer
from build.VPLParser import VPLParser
import myListener


def main(argv):
    char_stream = FileStream(argv[1])
    lexer = VPLLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = VPLParser(tokens)
    tree = parser.start()

    listener = myListener.myListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    for token in tokens.tokens:
        print("token: ", token.text)



if __name__ == '__main__':
    main(sys.argv)
