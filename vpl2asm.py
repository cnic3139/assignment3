#!/usr/bin/env python3
import sys
from antlr4 import *
from build.VPLLexer import VPLLexer
from build.VPLParser import VPLParser
import myListener


def main():
    for token in tokens.tokens:
        print("token: ", token.text)
    return
    file = open("out.s", "W+")
    # Iterate through parse tree, using template
    generatedText = genText()
    for line in generatedText:
        file.write(line)
    file.close()


def eventHandler(node, direction):
    parseTree.append((node, direction))


def genText():
    programList = []  # list of lines for program
    # Ensure first index in parseTree is start symb
    if parseTree[parseTreeIndex] != ("start", "enter"):
        sys.exit(1)
    parseTreeIndex += 1

    lineNo = 0
    lineNo = mHandler(programList, lineNo)

    return "\n".join(programList)


def mHandler(programList, lineNo):
    while True:
        if parseTree[parseTreeIndex] != ("m", "enter"):
            sys.exit(1)
        parseTreeIndex += 1

        if parseTree[parseTreeIndex] == ("m", "exit"):
            parseTreeIndex += 1
            break  # Out of infinite loop
        else:
            lineNo = function(programList, lineNo, tokensIndex)
    return lineNo


def addressCon(programList, lineNo, const, destreg):
    template = open("templates/t_address_con.asm", "r")
    for line in template.readlines():
        for word in line.split():
            if word == "<X>":
                word = const
            elif word == "$.const<X>,":
                word = "$.const" + const + ","
            elif word == "<destreg>":
                word = destreg
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo  # Lists pass by reference, ints by value


def addressVar(programList, lineNo, var, destReg):
    template = open("templates/t_address_var.asm", "r")
    for line in template.readlines():
        for word in line:
            if word == "$<N>,":
                word = "$" + var + ","
            elif word == "<destreg>":
                word = destReg
            elif word == "<destreg>,":
                word = destReg + ","
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


def addressVec(programList, lineNo, argReg, destReg):
    template = open("templates/t_address_vec.asm", "r")
    for line in template.readlines():
        for word in line.split():
            if word == "<argreg-N+1>,":
                word = argReg + ","
            elif word == "<destreg>":
                word = destReg
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


def allocate(programList, lineNo, num):
    # Add template in file at given lineNo

    # Determine number of local vars to allocate

    # Replace <NUM> with num of local vars to allocate
    template = open("templates/t_allocate.asm", "r")
    for line in template.readlines():
        for word in line:
            if word == "$<NUM>,":
                word = "$" + num + ","
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


def function(programList, lineNo, name):
    # Add template in file at given lineNo

    # Replace <name> with function name

    # In template, replace <allocate> with allocation of variables

    # In template, replaces <body> with body of function

    # TokensIndex should be at index of "func"

    if parseTree[parseTreeIndex] != ("f", "enter"):
        sys.exit(1)
    parseTreeIndex += 1

    template = open("templates/t_function.asm", "r")
    for line in template.readlines():
        for word in line:
            if word == "<name>":
                word = name
            elif word == "<name>:":
                word = name + ":"
            elif word == "<name>,":
                word = name + ","
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


def genConst(programList, lineNo, const):
    # Add template in file at given lineNo
    template = open("templates/t_gen_const.asm", "r")
    for line in template.readlines():
        for word in line:
            if word == ".const<X>:":
                word = ".const" + const + ":"
            elif word == "<X>":
                word = const
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


def identEqFactor():
    template = open("templates/t_ident_=_factor.asm", "r")
    # TODO
    template.close()


def identEqOpFactorFactor():
    template = open("templates/t_ident_=_op(factor,_factor).asm", "r")
    # TODO
    template.close()


def t_if():
    template = open("templates/t_if.asm", "r")
    # TODO
    template.close()


def t_sum():
    template = open("templates/t_sum.asm", "r")
    # TODO
    template.close()


def t_while():
    template = open("templates/t_while.asm", "r")
    # TODO
    template.close()


parseTree = []
parseTreeIndex = 0

char_stream = FileStream(sys.argv[1])
lexer = VPLLexer(char_stream)
tokens = CommonTokenStream(lexer)
tokensIndex = 0
parser = VPLParser(tokens)
tree = parser.start()
listener = myListener.myListener(eventHandler)
walker = ParseTreeWalker()
walker.walk(listener, tree)

if __name__ == '__main__':
    main()
