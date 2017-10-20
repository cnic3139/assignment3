#!/usr/bin/env python3
import sys
from antlr4 import *
from build.VPLLexer import VPLLexer
from build.VPLParser import VPLParser
import myListener


'''
Method: main
Parameters: none
Description: Main method, first function to be executed after code outside
 methods.
Returns: No value returned.
'''


def main():
    for token in tokens.tokens:
        print("token: ", token.text)
    return
    # output name should be same as input!
    
    file = open("out.s", "W+")
    # Iterate through parse tree, using template
    generatedText = genText()
    for line in generatedText:
        file.write(line)
    file.close()


'''
Method: eventHandler
Parameters: node (String), direction (String), ctsText (String)
Description: This method is called by methods of the "myListener" class to
 create a list (parseTree) representing the parse tree of the input VPL
 program.
Returns: No value returned.
'''


def eventHandler(node, direction, ctxText):
    # Listen for things here!
    parseTree.append((node, direction))
    ctxTree.append(ctxText)


'''
Method: genText
Parameters: None.
Description: Generates the text of the assembly program.
Returns: Program list as a string.
'''


def genText():
    programList = []  # list of lines for program
    # Ensure first index in parseTree is start symb
    if parseTree[parseTreeIndex] != ("start", "enter"):
        sys.exit(1)
    parseTreeIndex += 1

    lineNo = 0
    lineNo = mHandler(programList, lineNo)

    return "\n".join(programList)


'''
Method: mHandler
Parameters: programList (list), lineNo (integer)
Description: Handles the "M" nonterminal symbol in the grammar.
Returns: lineNo as an integer.
'''


def mHandler(programList, lineNo):
    funcNum = 0
    while True:
        if parseTree[parseTreeIndex] != ("m", "enter"):
            sys.exit(1)
        parseTreeIndex += 1

        if parseTree[parseTreeIndex] == ("m", "exit"):
            parseTreeIndex += 1
            break  # Out of infinite loop
        else:
            while tokens.tokens[tokensIndex] != "func":
                tokensIndex += 1
            tokensIndex += 1
            name = tokens.tokens[tokensIndex]
            lineNo = function(programList, lineNo, name, funcNum)
            funcNum += 1
    return lineNo


'''
Method: addressCon
Parameters: programList (list), lineNo (integer), const (number), destreg
 (register)
Description: Method used to write the template "t_address_con.asm" to file,
 filling in where necessary.
Returns: lineNo as an integer.
'''


def addressCon(programList, lineNo, const, destreg):
    template = open("templates/t_address_con.asm", "r")

    for line in template.readlines():
        for i, word in enumerate(line.split()):
            if word == "<X>":
                line[i] = const
            elif word == "$.const<X>,":
                line[i] = "$.const" + const + ","
            elif word == "<destreg>":
                line[i] = destreg
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo  # Lists pass by reference, ints by value


'''
Method: addressVar
Parameters: programList (list), lineNo (integer), var (string), destReg
 (register)
Description: Method used to write the template "t_address_var.asm" to file,
 filling in where necessary.
Returns: lineNo as an integer.
'''


def addressVar(programList, lineNo, var, destReg):
    template = open("templates/t_address_var.asm", "r")
    for line in template.readlines():
        for i, word in enumerate(line.split()):
            if word == "$<N>,":
                line[i] = "$" + var + ","
            elif word == "<destreg>":
                line[i] = destReg
            elif word == "<destreg>,":
                line[i] = destReg + ","
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


'''
Method: addressVec
Parameters: programList (list), lineNo (integer), argReg (register), destReg
 (register)
Description: Method used to write the template "t_address_vec.asm" to file,
 filling in where necessary.
Returns: lineNo as an integer.
'''


def addressVec(programList, lineNo, argReg, destReg):
    template = open("templates/t_address_vec.asm", "r")
    for line in template.readlines():
        for i, word in enumerate(line.split()):
            if word == "<argreg-N+1>,":
                line[i] = argReg + ","
            elif word == "<destreg>":
                line[i] = destReg
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


'''
Method: allocate
Parameters: programList (list), lineNo (integer), num (number)
Description: Method used for allocating local variables in a function, based
 on the template "t_allocate.asm"
Returns: lineNo as an integer.
'''


def allocate(programList, lineNo, num):
    # Add template in file at given lineNo

    # Determine number of local vars to allocate

    # Replace <NUM> with num of local vars to allocate
    template = open("templates/t_allocate.asm", "r")
    for line in template.readlines():
        for i, word in enumerate(line.split()):
            if word == "$<NUM>,":
                line[i] = "$" + num + ","
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


'''
Method: function
Parameters: programList (list), lineNo (integer), name (string), funcNum
 (integer)
Description: Method used for writing a function definition, based on the
 template "t_function.asm"
Returns: lineNo as an integer.
'''


def function(programList, lineNo, name, funcNum):
    # Add template in file at given lineNo

    # Replace <name> with function name

    # In template, replace <allocate> with allocation of variables

    # In template, replaces <body> with body of function

    # tokensIndex should be at index of "func"

    if parseTree[parseTreeIndex] != ("f", "enter"):
        sys.exit(1)
    parseTreeIndex += 1

    # SECTION FOR GETTING PARS & VARS IN LIST =================================
    listPars = []
    listVars = []

    # At this point tokensIndex should be pointing at the function name
    # So we want to traverse the parameters and add them to listPars, with
    #  the parameter as key and index as value
    tokensIndex += 1
    if tokens.tokens[tokensIndex] != "(":
        print("Something went wrong in method 'function'")
        sys.exit(1)
    tokensIndex += 1
    while tokens.tokens[tokensIndex] != ")":
        if tokens.tokens[tokensIndex] != ",":
            listPars.append(tokens.tokens[tokensIndex])
        tokensIndex += 1

    # After that should come the declaration of variables, so we can traverse
    #  this and add them to listVars in the same way as the parameters
    # tokensIndex should be pointing at ")" now
    # So next token should be "var" if there are variables declared
    tokensIndex += 1
    if tokens.tokens[tokensIndex] == 'var':
        tokensIndex += 1
        while tokens.tokens[tokensIndex] != ";":
            if tokens.tokens[tokensIndex] != ',':
                listVars.append(tokens.tokens[tokensIndex])

    # SECTION FOR GETTING PARS & VARS IN LIST =================================

    template = open("templates/t_function.asm", "r")
    templateInserted = False
    for line in template.readlines():
        for i, word in enumerate(line.split()):
            templateInserted = False
            if word == "<name>":
                line[i] = name
            elif word == "<name>:":
                line[i] = name + ":"
            elif word == "<name>,":
                line[i] = name + ","
            elif word == "<allocate>":
                # Look over tokens - between var & ;, number of tokens
                #  (excluding ',') is the number of variables to be declared
                templateInserted = True
                lineNo = allocate(programList, lineNo, len(listVars))
            elif word == "<insert>":
                templateInserted = True
                # TODO
                sIndex = parseTree.index(("s", "enter"))
                sString = ctxTree[sIndex]
                if sString.startswith("if"):
                    t_if(programList, lineNo)
                elif sString.startswith("while"):
                    t_while(programList, lineNo)
                else:
                    # Must start with IDENT
                    pass
        if templateInserted:
            programList.insert(lineNo + 1, "\n")
        else:
            programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


'''
Method: genConst
Parameters: programList (list), lineNo (integer), const (number)
Description: Method used for allocating memory for a constant numerical value,
 based on the template "t_gen_const.asm"
Returns: lineNo as an integer.
'''


def genConst(programList, lineNo, const):
    # Add template in file at given lineNo
    template = open("templates/t_gen_const.asm", "r")
    for line in template.readlines():
        for i, word in enumerate(line.split()):
            if word == ".const<X>:":
                line[i] = ".const" + const + ":"
            elif word == "<X>":
                line[i] = const
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


'''
Method: identEqFactor
Parameters: programList (list), lineNo (integer)
Description: Method used to write the template "t_ident_=_factor.asm" to file,
 filling in where necessary.
Returns: lineNo as an integer.
'''


def identEqFactor(programList, lineNo):
    template = open("templates/t_ident_=_factor.asm", "r")
    for line in template.readlines():
        for i, word in enumerate(line.split()):
            if word == "<load-rax>":
                line[i] = ""  # TODO
            elif word == "<load-r10>":
                line[i] = ""  # TODO
            elif word == ".loop-end<X>":
                line[i] = ".loop-end" + num
            elif word == ".loop-end<X>:":
                line[i] = ".loop-end" + num + ":"
            elif word == ".loop-begin<X>":
                line[i] = ".loop-begin" + num
            elif word == ".loop-begin<X>:":
                line[i] = ".loop-begin" + num + ":"
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


'''
Method: identEqOpFactorFactor
Parameters: programList (list), lineNo (integer), num (number)
Description: Method used to write the template
 "t_ident_=_op(factor,_factor).asm" to file, filling in where necessary.
Returns: lineNo as an integer.
'''


def identEqOpFactorFactor(programList, lineNo, num):
    template = open("templates/t_ident_=_op(factor,_factor).asm", "r")
    for line in template.readlines():
        for i, word in enumerate(line.split()):
            if word == "<load-source1-rax>":
                line[i] = ""  # TODO
            elif word == "<load-source2-r10>":
                line[i] = ""  # TODO
            elif word == "<load-dest-r11>":
                line[i] = ""  # TODO
            elif word == ".loop-begin<X>":
                line[i] = ".loop-begin" + num
            elif word == ".loop-begin<X>:":
                line[i] = ".loop-begin" + num + ":"
            elif word == ".loop-end<X>":
                line[i] = ".loop-end" + num
            elif word == ".loop-end<X>:":
                line[i] = ".loop-end" + num + ":"
            elif word == "<operation>":
                line[i] = ""
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


'''
Method: t_if
Parameters: programList (list), lineNo (integer)
Description: Method used to write the template "t_if.asm" to file,
 filling in where necessary.
Returns: lineNo as an integer.
'''


def t_if(programList, lineNo):
    template = open("templates/t_if.asm", "r")
    for line in template.readlines():
        for i, word in enumerate(line.split()):
            if word == "<template>":
                line[i] = ""  # TODO
            elif word == "<true-branch>":
                line[i] = ""  # TODO
            elif word == "<false-branch>":
                line[i] = ""  # TODO
            elif word == ".true-branch<NUM>":
                line[i] = ".true-branch" + num
            elif word == ".false-branch<NUM>":
                line[i] = ".false-branch" + num
            elif word == ".endif<NUM>":
                line[i] = ".endif" + num
            elif word == ".endif<NUM>:":
                line[i] = ".endif" + num + ":"
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


'''
Method: t_sum
Parameters: programList (list), lineNo (integer), num (number)
Description: Method used to write the template "t_sum.asm" to file,
 filling in where necessary.
Returns: lineNo as an integer.
'''


def t_sum(programList, lineNo, num):
    template = open("templates/t_sum.asm", "r")
    for line in template.readlines():
        for i, word in enumerate(line.split()):
            if word == "<load-source-rax>":
                line[i] = ""  # TODO
            elif word == ".loop-begin<X>":
                line[i] = ".loop-begin" + num
            elif word == ".loop-begin<X>:":
                line[i] = ".loop-begin" + num + ":"
            elif word == ".loop-end<X>":
                line[i] = ".loop-end" + num
            elif word == ".loop-end<X>:":
                line[i] = ".loop-end" num + ":"
            elif word == "<true>":
                line[i] = ""  # TODO
            elif word == "<false>":
                line[i] = ""  # TODO
            elif word == "<NUMBER>":
                line[i] = ""  # TODO
            elif word == ".L<NUMBER>:":
                line[i] = ""  # TODO
            elif word == ".L<NUMBER>,":
                line[i] = ""  # TODO
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo


'''
Method: t_while
Parameters: programList (list), lineNo (integer), num (number)
Description: Method used to write the template "t_while.asm" to file,
 filling in where necessary.
Returns: lineNo as an integer.
'''


def t_while(programList, lineNo, num):
    template = open("templates/t_while.asm", "r")
    for line in template.readlines():
        for i, word in enumerate(line.split()):
            if word == ".loopcond<NUM>":
                line[i] = ".loopcond" + num
            elif word == ".loopcond<NUM>:":
                line[i] = ".loopcond" + num + ":"
            elif word == ".loopbegin<NUM>":
                line[i] = ".loopbegin" + num
            elif word == ".loopend<NUM>":
                line[i] = ".loopend" + num
            elif word == "<loop-body>":
                line[i] = ""  # TODO
            elif word == "<template>":
                line[i] = ""  # TODO
        programList.insert(lineNo + 1, line)
        lineNo += 1
    template.close()
    return lineNo

'''
Set-up code used to initalise ANTLR-related objects, as well as declare
 global variables needed in multiple functions
'''
parseTree = []
parseTreeIndex = 0
ctxTree = []

ifCount = 0
whileCount = 0

nP = False
funcPars = []
funcVars = []

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
