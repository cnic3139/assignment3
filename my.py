#!/usr/bin/env python3
import sys
from antlr4 import *
from build.VPLLexer import VPLLexer
from build.VPLParser import VPLParser
import myListener

nodes = {}
vals = {}
valCounter = 0

pars = []
varis = []
consts = []

registers = ["rdi", "rsi", "rdx", "rcx", "r8", "r9"]

inP = False
inD = False

finalCode = None


def enter(node, ctx):
    # General pre-stuff goes here =============================================
    myList = []
    # This is where you will store your value
    # Try and get it from parent or make it yourself
    myNum = None
    if inP or inD:
        return
    print(inP, inD)
    if ctx.parentCtx is not None:  # To deal with root node
        if len(nodes[ctx.parentCtx]) == 1:
            return
        parentDeps = nodes[ctx.parentCtx][1]
        for dep in parentDeps:
            if vals[dep] is None:
                myNum = dep
                break
    if myNum is None:
        myNum = getVal()
    print(node, myNum)
    myList.append(myNum)  # myList[0] is where value is located
    vals[myList[-1]] = None  # Initialise with 'None' value
    # General pre-stuff goes here =============================================

    # Node-specific stuff - use selector to defer to nodes ====================
    myList = selector(node, "enter", ctx, myList)
    # Node-specific stuff - use selector to defer to nodes ====================

    # General post-stuff goes here ============================================
    # Store this list in nodes with ctx as key
    nodes[ctx] = myList
    # General post-stuff goes here ============================================


def exit(node, ctx):
    # General pre-stuff goes here =============================================
    if ctx not in nodes.keys():
        return
    myData = nodes[ctx]
    # General pre-stuff goes here =============================================

    # Node - specific stuff  - use selector to defer to nodes =================
    myList = selector(node, "exit", ctx, myData)
    # Node - specific stuff  - use selector to defer to nodes =================

    # General post-stuff goes here ============================================
    nodes[ctx] = myList
    # General post-stuff goes here ============================================


def selector(node, direct, ctx, pList):
    if node == "start":
        return start(direct, ctx, pList)
    elif node == "m":
        return m(direct, ctx, pList)
    elif node == "f":
        return f(direct, ctx, pList)
    elif node == "p":
        return p(direct, ctx, pList)
    elif node == "l":
        return l(direct, ctx, pList)
    elif node == "d":
        return d(direct, ctx, pList)
    elif node == "s":
        return s(direct, ctx, pList)
    elif node == "r":
        return r(direct, ctx, pList)
    elif node == "e":
        return e(direct, ctx, pList)
    elif node == "c":
        return c(direct, ctx, pList)
    elif node == "ident":
        return ident(direct, ctx, pList)
    elif node == "num":
        return num(direct, ctx, pList)


def start(direct, ctx, pList):
    global finalCode
    myList = pList
    if direct == "enter":
        # Reinitialise objects
        nodes = {}
        vals = {}
        pars = []
        varis = []
        consts = []
        addVar("__TEMP__")  # Special variable for calculations
        finalCode = None
        myList.append(getDependencies(1))
        myList.append("start")
    elif direct == "exit":
        fileName = sys.argv[1].strip(".vpl")
        print("*******************************************FILENAME:", filename)
        file = open(fileName + ".s", "w")
        file.write(finalCode)
        file.close()
    return myList


def m(direct, ctx, pList):
    global finalCode
    myList = pList
    if direct == "enter":
        myList.append(getDependencies(1))
        myList.append("m")
    elif direct == "exit":
        dep = vals[myList[1][0]][0]
        tem = vals[myList[1][0]][1]

        template = tem

        tempVal = vals[myList[0]]
        vals[myList[0]] = []
        vals[myList[0]].append(tempVal)
        vals[myList[0]].append(template)

        if vals[mylist[0]][0] is None:
            vals[myList[0]][0] = "none"

        finalCode = template
        print(finalCode)

    return myList


def allocate():
    template = getFileAsString("templates/t_allocate.asm")
    template.replace("<NUM>", str(len(varis)))
    return template


def f(direct, ctx, pList):
    myList = pList
    if direct == "enter":
        myList.append(getDependencies(2))  # Just ident and S, P, D don't do code
        myList.append("func")
    elif direct == "exit":
        # S has to return have a list in its return so we don't need to check
        dep1 = vals[myList[1][0]]
        print("mylist", myList)
        print("vals", vals[myList[1][1]])
        dep2 = vals[myList[1][1]][0]
        tem2 = vals[myList[1][1]][1]

        template = getFileAsString("templates/t_function.asm")
        template.replace("<name>", ctx.getText()[4:].split("(")[0])
        template.replace("<allocate>", allocate())
        template.replace("<insert>", tem2)

        # Change list[0] to list, 0 = depVal, 1 = assembly template
        tempVal = vals[myList[0]]
        vals[myList[0]] = []
        vals[myList[0]].append(tempVal)
        vals[myList[0]].append(template)

    if vals[myList[0]][0] is None:
        vals[myList[0]][0] = "none"

    return myList


def p(direct, ctx, pList):
    global inP
    myList = pList
    if direct == "enter":
        inP = True
        pass
    elif direct == "exit":
        inP = False
        pass
    return myList


def l(direct, ctx, pList):
    global inP
    global inD
    myList = pList
    if direct == "enter":
        if inP:
            addPar(ctx.start.text)
        elif inD:
            addVar(ctx.start.text)
    elif direct == "exit":
        pass
    return myList


def d(direct, ctx, pList):
    global inD
    myList = pList
    if direct == "enter":
        inD = True
        pass
    elif direct == "exit":
        inD = False
        pass


def s(direct, ctx, pList):
    myList = pList
    if direct == "enter":
        # Need to find out which branch to follow
        # Because of Node R, there's an extra dependency for things
        text = ctx.start.text
        tmplist = ["", "endif", "endwhile", "end", ";"]
        if text == "if":
            myList.append(getDependencies(3))
            myList.append("if")
        elif text == "while":
            myList.append(getDependencies(3))
            myList.append("while")
        elif text in tmplist:
            # Epsilon (Actually R)
            myList.append(getDependencies(1))
            myList.append("epsilon")
            pass
        else:  # text == ident
            myList.append(getDependencies(3))
            myList.append("ident")

    elif direct == "exit":
        myData = nodes[ctx]

        dep1 = None
        dep2 = None
        dep3 = None
        tem1 = None
        tem2 = None
        tem3 = None

        if vals[myData[1][0]] is list:
            dep1 = vals[myData[1][0]][0]
            tem1 = vals[myData[1][0]][1]
        else:
            dep1 = vals[myData[1][0]]

        if len(myData[1]) >= 2:
            if vals[myData[1][1]] is list:
                dep2 = vals[myData[1][1]][0]
                tem2 = vals[myData[1][1]][1]
            else:
                dep2 = vals[myData[1][1]]

        if len(myData[1]) >= 3:
            if vals[myData[1][2]] is list:
                dep3 = vals[myData[1][2]][0]
                tem3 = vals[myData[1][2]][1]
            else:
                dep3 = vals[myData[1][2]]

        # WHILE AND IF NEED TO REPLACE <TRUE> AND <FALSE> IN C TEMPLATE
        # C will be the first dependency in both IF and WHILE

        num = getVal()

        if myData[2] == "if":
            tem1.replace("<true>", ".true-branch<NUM>")
            tem1.replace("<false>", ".false-branch<NUM>")

            template = getFileAsString("templates/t_if.asm")
            template.replace("<template>", tem1)
            template.replace("<NUM>", str(num))
            template.replace("<true-branch>", tem2)
        elif myData[2] == "while":
            tem1.replace("<true>", ".loopbegin<NUM>")
            tem1.replace("<false>", ".loopend<NUM>")

            template = getFileAsString("templates/t_while.asm")
            template.replace("<template>", tem1)
            template.replace("<NUM>", str(num))
            template.replace("<loop-body>", tem2)
        elif myData[2] == "epsilon":
            template = tem1
        elif myData[2] == "ident":
            template = getFileAsString("templates/t_ident_=_factor.asm")
            template.replace("<load-rax>", load("__TEMP__", "rax"))
            template.replace("<load-r10>", load("dep1", "r10"))
            template.replace("<X>", str(num))

        # Concaternate templates
        # tem3 = R template if it exists
        # tem2 = loop body template if it exists
        # tem1 = IDENT or condition template
        # So tem3 should come last
        # tem2 and tem1 shouldnt go anywhere if they were in IF or WHILE
        if myData[2] == "if" or myData[2] == "while":
            if tem3 is not None:
                template = template + tem3
        if myData[2] == "ident":
            if tem3 is not None:
                template = template + tem3
            if tem2 is not None:
                template = tem2 + template

        # Change list[0] to list, 0 = depVal, 1 = assembly template
        tempVal = vals[myData[0]]
        vals[myData[0]] = []
        vals[myData[0]].append(tempVal)
        vals[myData[0]].append(template)

        myList = myData

    if vals[mylist[0]][0] is None:
        vals[myList[0]][0] = "none"

    return myList


def r(direct, ctx, pList):
    myList = pList
    if direct == "enter":
        myList.append(getDependencies(1))
        myList.append("s")
    elif direct == "exit":
        pass
    return myList


def getOp(ctx):
    text = cts.start.text
    if text == "add":
        return "addps"
    elif text == "min":
        return "minps"
    elif text == "mult":
        return "mulps"
    elif text == "div":
        return "divps"
    elif text == "min":
        return "minps"


def load(value, register):
    # Need to inspect value to decide which template to use
    if value.isnumeric():  # Constant
        template = getFileAsString("templates/t_address_con.asm")
        template.replace("<X>", value)
        template.replace("<destreg>", "%" + register)
        return template
    elif value in varis:  # Variable
        template = getFileAsString("templates/t_address_var.asm")
        template.replace("<N>", str(varis.index(value) + 1))
        template.replace("<destreg>", "%" + register)
        return template
    elif value in pars:  # Parameter
        template = getFileAsString("templates/t_address_vec.asm")
        template.replace("<argreg-N+1>",
                         "%" + registers[pars.index(value) + 1])
        template.replace("<destreg>", "%" + register)
        return template


def e(direct, ctx, pList):
    myList = pList
    if direct == "enter":

        # Need to find out which branch to follow
        text = ctx.start.text
        if text == "add":
            # This is where you will store your dependencies
            # myList[1] is list of dependencies
            myList.append(getDependencies(2))
            myList.append("op")
        elif text == "minus":
            myList.append(getDependencies(2))
            myList.append("op")
        elif text == "mult":
            myList.append(getDependencies(2))
            myList.append("op")
        elif text == "div":
            myList.append(getDependencies(2))
            myList.append("op")
        elif text == "min":
            myList.append(getDependencies(2))
            myList.append("op")
        elif text == "(":
            myList.append(getDependencies(1))
            myList.append("e")
        elif text.isnumeric():  # text == num
            myList.append(getDependencies(1))
            myList.append("num")
        else:  # text == ident
            myList.append(getDependencies(1))
            myList.append("ident")

    elif direct == "exit":
        # Lookup in node, get data from when you entered this node
        myData = nodes[ctx]
        print("==============", myData[0])
        print("--------------", vals[myData[0]])
        # STILL NEED TO CHECK IF DEPENDENTS HAVE CODE SNIPPETS
        dep1 = None
        dep2 = None
        tem1 = None
        tem2 = None

        if vals[myData[1][0]] is list:
            dep1 = vals[myData[1][0]][0]
            tem1 = vals[myData[1][0]][1]
        else:
            dep1 = vals[myData[1][0]]

        if len(myData[1]) >= 2:
            if vals[myData[1][1]] is list:
                dep2 = vals[myData[1][1]][0]
                tem2 = vals[myData[1][1]][1]
            else:
                dep2 = vals[myData[1][1]]

        template = None
        if myData[2] == "op":
            template = getFileAsString("templates/t_ident_=_op(factor,_factor).asm")
            template.replace("<load-source1-rax>", load(dep1, "rax"))
            template.replace("<load-source2-r10>", load(dep2, "r10"))
            template.replace("<load-dest-r11>", load("__TEMP__", "r11"))
            template.replace("<operation>", getOp(ctx))
            template.replace("<X>", str(getVal()))

            # If const, need to remove lines in template
            if vals[myData[1][0]].isnumeric():
                template.replace("addq   $16,    " + "%" + "rax", "")

            if vals[myData[1][1]].isnumeric():
                template.replace("addq   $16,    " + "%" + "r10", "")

        elif myData[2] == "e":
            pass  # I dunno what to do here, just give all its stuff to parent?
        elif myData[2] == "num" or myData[2] == "ident":
            template = getFileAsString("templates/t_ident_=_factor.asm")
            template.replace("<load-rax>", load(dep1, "rax"))
            template.replace("<load-r10>", load("__TEMP__", "r10"))
            template.replace("<X>", str(getVal()))

            # If const, need to remove lines in template
            if myData == "num":
                template.replace("addq   $16,    " + "%" + "rax", "")

        # Concaternate templates
        if tem2 is not None:
            template = tem2 + template
        if tem1 is not None:
            template = tem1 + template

        # Change list[0] to list, 0 = depVal, 1 = assembly template
        tempVal = vals[myData[0]]
        print("TEMPVAL", tempVal)
        vals[myData[0]] = []
        vals[myData[0]].append(tempVal)
        vals[myData[0]].append(template)

        myList = myData

    if vals[mylist[0]][0] is None:
        vals[myList[0]][0] = "none"

    return myList


def c(direct, ctx, pList):
    myList = pList
    if direct == "enter":
        myList.append(getDependencies(2))
        if "<" in ctx.getText():
            myList.append("less")
        elif ">" in ctx.getText():
            myList.append("greater")
    elif direct == "exit":

        dep = None
        tem = None
        print("here!", vals[myList[1][0]])
        if isinstance(vals[myList[1][0]], list):
            print("this")
            dep = vals[myList[1][0]][0]
            tem = vals[myList[1][0]][1]
        else:
            print("that")
            dep = vals[myList[1][0]]
            print(type(dep))
            print(vals[myList[1][0]] is list)
        print("dep", dep)
        template = getFileAsString("templates/t_sum.asm")
        template.replace("<load-source-rax>", load("__TEMP__", "rax"))
        template.replace("<X>", str(getVal()))
        template.replace("<NUMBER>", vals[myList[1][1]])
        if dep.isnumeric():
            template.replace("addq    $16,    " + "%" + "rax", "")

        # Concaternate templates
        if tem is not None:
            template = tem + template

        # Change list[0] to list, 0 = depVal, 1 = assembly template
        tempVal = vals[myList[0]]
        vals[myList[0]] = []
        vals[myList[0]].append(tempVal)
        vals[myList[0]].append(template)

    if vals[mylist[0]][0] is None:
        vals[myList[0]][0] = "none"

    return myList


def ident(direct, ctx, pList):
    myList = pList
    if direct == "enter":
        myList.append(getDependencies(0))
        myList.append(ctx.start.text)
    elif direct == "exit":
        # Defer finding out par vs var for later
        #  I still need the text at this point
        vals[myList[0]] = myList[2]
    return myList


def num(direct, ctx, pList):
    myList = pList
    if direct == "enter":
        myList.append(getDependencies(0))
        myList.append(ctx.start.text)
        addConst(myList[2])
    elif direct == "exit":
        if myList[2] in consts:
            vals[myList[0]] = myList[2]
    return myList


def getFileAsString(path):
    file = open(path, "r")
    string = file.read()
    file.close()
    return string


def getVal():
    global valCounter
    returnVal = valCounter
    valCounter += 1
    return returnVal


def getDependencies(num):
    returnList = []
    for i in range(num):
        returnList.append(getVal())
        vals[returnList[-1]] = None
    return returnList


def addPar(par):
    if par not in pars:
        pars.append(par)


def addVar(var):
    if var not in varis:
        varis.append(var)


def addConst(const):
    if const not in consts:
        consts.append(const)


def dispatcher(node, direct, ctx):

    if direct == "enter":
        enter(node, ctx)
    elif direct == "exit":
        exit(node, ctx)

char_stream = FileStream(sys.argv[1])
lexer = VPLLexer(char_stream)
tokens = CommonTokenStream(lexer)
parser = VPLParser(tokens)
root = parser.start()

listener = myListener.myListener(dispatcher)
walker = ParseTreeWalker()
walker.walk(listener, root)
