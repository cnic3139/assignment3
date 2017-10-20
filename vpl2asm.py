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
    # output name should be same as input!

    print("\ngentext len\n")
    file = open("out.s", "w")

    # Iterate through parse tree, using template
    generatedText = genText()
    print("\ngentext len\n", len(generatedText))
    for line in generatedText:
        file.write(line)
        file.write("hello")
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
    global parseTreeIndex
    programList = []  # list of lines for program
    # Ensure first index in parseTree is start symb
    if parseTree[parseTreeIndex] != ("start", "enter"):
        print("System exit genText")
        sys.exit(1)
    parseTreeIndex += 1

    lineNo = 0
    print("Error mHandler")
    lineNo = mHandler(programList, lineNo)
    print("Error mHandler2")

    return "\n".join(programList)


'''
Method: mHandler
Parameters: programList (list), lineNo (integer)
Description: Handles the "M" nonterminal symbol in the grammar.
Returns: lineNo as an integer.
'''


def mHandler(programList, lineNo):
    global parseTreeIndex, tokensIndex
    funcNum = 0
    while True:
        print("parse pair", parseTree[parseTreeIndex], parseTreeIndex)

        # if parseTree[parseTreeIndex] != ("m", "enter"):
        #     print("System Exit mHandler")
        #     sys.exit(1)
        parseTreeIndex += 1

        if parseTree[parseTreeIndex] == ("m", "exit"):
            parseTreeIndex += 1
            break  # Out of infinite loop
        else:
            print(tokensIndex)
            print(tokens.tokens[tokensIndex].text)
            while tokensIndex < len(tokens.tokens):
                print("tokenI: {0}, token: {1}".format(tokensIndex, tokens.tokens[tokensIndex].text))
                if tokens.tokens[tokensIndex].text != "func":
                    tokensIndex += 1
                else:
                    tokensIndex += 1
                    name = tokens.tokens[tokensIndex].text
                    print("mHandler Function Call")
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
        tempLine = []
        for i, word in enumerate(line.split()):
            if word == "<X>":
                tempLine.append(const)
            elif word == "$.const<X>,":
                tempLine.append("$.const" + const + ",")
            elif word == "<destreg>":
                tempLine.append(destreg)
        line = tempLine
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
        tempLine = []
        for i, word in enumerate(line.split()):
            if word == "$<N>,":
                tempLine.append("$" + var + ",")
            elif word == "<destreg>":
                tempLine.append(destReg)
            elif word == "<destreg>,":
                tempLine.append(destReg + ",")
        line = tempLine
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
        tempLine = []
        for i, word in enumerate(line.split()):
            if word == "<argreg-N+1>,":
                tempLine.append(argReg + ",")
            elif word == "<destreg>":
                tempLine.append(destReg)
        line = tempLine
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
        tempLine = []
        for i, word in enumerate(line.split()):
            if word == "$<NUM>,":
                tempLine.append("$" + str(num) + ",")
        line = tempLine
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
    global parseTreeIndex, tokensIndex
    # Add template in file at given lineNo

    # Replace <name> with function name

    # In template, replace <allocate> with allocation of variables

    # In template, replaces <body> with body of function

    # tokensIndex should be at index of "func"
    print("Function called!", parseTree[parseTreeIndex], parseTreeIndex)

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
    if tokens.tokens[tokensIndex].text != "(":
        print("Something went wrong in method 'function'")
        sys.exit(1)
    tokensIndex += 1
    while tokens.tokens[tokensIndex].text != ")":
        if tokens.tokens[tokensIndex].text != ",":
            listPars.append(tokens.tokens[tokensIndex].text)
        tokensIndex += 1

    # After that should come the declaration of variables, so we can traverse
    #  this and add them to listVars in the same way as the parameters
    # tokensIndex should be pointing at ")" now
    # So next token should be "var" if there are variables declared
    tokensIndex += 1
    if tokens.tokens[tokensIndex].text == 'var':
        tokensIndex += 1
        while tokens.tokens[tokensIndex].text != ";":
            if tokens.tokens[tokensIndex].text != ',':
                listVars.append(tokens.tokens[tokensIndex].text)
    tokensIndex = 0

    # SECTION FOR GETTING PARS & VARS IN LIST =================================

    template = open("templates/t_function.asm", "r")
    templateInserted = False
    # i = 0
    for line in template.readlines():
        # if i > 1:
            # break
        tempLine = []
        for i, word in enumerate(line.split()):
            # print("\nLINE\n", line)
            # print(line[i], i)
            # print("word:", word)
            # print("name:", name)
            templateInserted = False
            if word == "<name>":
                tempLine.append(name)
            elif word == "<name>:":
                tempLine.append(name + ":")
            elif word == "<name>,":
                tempLine.append(name + ",")
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
            else:
                tempLine.append(word)
        print("FINAL LINE: ", tempLine)
        line = tempLine
        if templateInserted:
            programList.insert(lineNo + 1, "\n")
        else:
            programList.insert(lineNo + 1, line)
        lineNo += 1
        # i += 1
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
        tempLine = []
        for i, word in enumerate(line.split()):
            if word == ".const<X>:":
                tempLine.append(".const" + const + ":")
            elif word == "<X>":
                tempLine.append(const)
        line = tempLine
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
        tempLine = []
        for i, word in enumerate(line.split()):
            if word == "<load-rax>":
                tempLine.append("")  # TODO
            elif word == "<load-r10>":
                tempLine.append("")  # TODO
            elif word == ".loop-end<X>":
                tempLine.append(".loop-end" + num)
            elif word == ".loop-end<X>:":
                tempLine.append(".loop-end" + num + ":")
            elif word == ".loop-begin<X>":
                tempLine.append(".loop-begin" + num)
            elif word == ".loop-begin<X>:":
                tempLine.append(".loop-begin" + num + ":")
        line = tempLine
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
        tempLine = []
        for i, word in enumerate(line.split()):
            if word == "<load-source1-rax>":
                tempLine.append("")  # TODO
            elif word == "<load-source2-r10>":
                tempLine.append("")  # TODO
            elif word == "<load-dest-r11>":
                tempLine.append("")  # TODO
            elif word == ".loop-begin<X>":
                tempLine.append(".loop-begin" + num)
            elif word == ".loop-begin<X>:":
                tempLine.append(".loop-begin" + num + ":")
            elif word == ".loop-end<X>":
                tempLine.append(".loop-end" + num)
            elif word == ".loop-end<X>:":
                tempLine.append(".loop-end" + num + ":")
            elif word == "<operation>":
                tempLine.append("")
        line = tempLine
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
        tempLine = []
        for i, word in enumerate(line.split()):
            if word == "<template>":
                tempLine.append("")  # TODO
            elif word == "<true-branch>":
                tempLine.append("")  # TODO
            elif word == "<false-branch>":
                tempLine.append("")  # TODO
            elif word == ".true-branch<NUM>":
                tempLine.append(".true-branch" + num)
            elif word == ".false-branch<NUM>":
                tempLine.append(".false-branch" + num)
            elif word == ".endif<NUM>":
                tempLine.append(".endif" + num)
            elif word == ".endif<NUM>:":
                tempLine.append(".endif" + num + ":")
        line = tempLine
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
        tempLine = []
        for i, word in enumerate(line.split()):
            if word == "<load-source-rax>":
                tempLine.append("")  # TODO
            elif word == ".loop-begin<X>":
                tempLine.append(".loop-begin" + num)
            elif word == ".loop-begin<X>:":
                tempLine.append(".loop-begin" + num + ":")
            elif word == ".loop-end<X>":
                tempLine.append(".loop-end" + num)
            elif word == ".loop-end<X>:":
                tempLine.append(".loop-end" + num + ":")
            elif word == "<true>":
                tempLine.append("")  # TODO
            elif word == "<false>":
                tempLine.append("")  # TODO
            elif word == "<NUMBER>":
                tempLine.append("")  # TODO
            elif word == ".L<NUMBER>:":
                tempLine.append("")  # TODO
            elif word == ".L<NUMBER>,":
                tempLine.append("")  # TODO
        line = tempLine
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
        tempLine = []
        for i, word in enumerate(line.split()):
            if word == ".loopcond<NUM>":
                tempLine.append(".loopcond" + num)
            elif word == ".loopcond<NUM>:":
                tempLine.append(".loopcond" + num + ":")
            elif word == ".loopbegin<NUM>":
                tempLine.append(".loopbegin" + num)
            elif word == ".loopend<NUM>":
                tempLine.append(".loopend" + num)
            elif word == "<loop-body>":
                tempLine.append("")  # TODO
            elif word == "<template>":
                tempLine.append("")  # TODO
        line = tempLine
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
