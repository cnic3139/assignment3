#!/usr/bin/env python3
import sys
import antlr4
from build.VPLLexer import VPLLexer
from build.VPLParser import VPLParser
from build.VPLListener import VPLListener


def main(argv):
    char_stream = antlr4.FileStream(argv[1])
    lexer = VPLLexer(char_stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = VPLParser(tokens)
    root = parser.start()
    print(root)

if __name__ == '__main__':
    main(sys.argv)
