import sys
from antlr4 import *
from build.VPLLexer import VPLLexer
from build.VPLParser import VPLParser
import myListener

char_stream = FileStream(sys.argv[1])
lexer = VPLLexer(char_stream)
tokens = CommonTokenStream(lexer)
parser = VPLParser(tokens)
root = parser.start()


def tmp(one, two, three):
    pass

listener = myListener.myListener(tmp)
walker = ParseTreeWalker()
walker.walk(listener, root)

nodes = {}
vals = {}
valCounter = 0

pars = []
varis = []
consts = []

registers = ["rdi", "rsi", "rdx", "rcx", "r8", "r9"]

inP = False
inD = False


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

    if node == "start":
        start(direct, ctx)
    elif node == "m":
        m(direct, ctx)
    if node == "f":
        f(direct, ctx)
    if node == "p":
        p(direct, ctx)
    if node == "l":
        l(direct, ctx)
    if node == "d":
        d(direct, ctx)
    if node == "s":
        s(direct, ctx)
    if node == "r":
        r(direct, ctx)
    if node == "e":
        e(direct, ctx)
    if node == "c":
        c(direct, ctx)
    if node == "ident":
        ident(direct, ctx)
    if node == "num":
        num(direct, ctx)


def enter(node, ctx):
    # General pre-stuff goes here =============================================
    myList = []
    # This is where you will store your value
    # Try and get it from parent or make it yourself
    myNum = None
    if ctx.parentCtx is not None:  # To deal with root node
        parentDeps = nodes[ctx.parentCtx][1]
        for dep in parentDeps:
            if vals[dep] is None:
                myNum = dep
                break
    if myNum is None:
        myNum = getVal()
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
    myData = nodes[ctx]

    myVal = myData[0]

    myDeps = myData[1]

    myCalc = myData[2]
    # General pre-stuff goes here =============================================

    # USE formula in myCalc with vars in myDeps to put val in myVal

    # Node - specific stuff  - use selector to defer to nodes =================
    myList = selector(node, "exit", ctx, myData)
    # Node - specific stuff  - use selector to defer to nodes =================

    # General post-stuff goes here ============================================
    nodes[ctx] = myList
    # General post-stuff goes here ============================================


def selector(node, direct, ctx, list):
    return {
        "start": start(direct, ctx),
        "m": m(direct, ctx),
        "f": f(direct, ctx),
        "p": p(direct, ctx),
        "l": l(direct, ctx),
        "d": d(direct, ctx),
        "s": s(direct, ctx),
        "r": r(direct, ctx),
        "e": e(direct, ctx),
        "c": c(direct, ctx),
        "ident": ident(direct, ctx),
        "num": num(direct, ctx),
    }[node]


def start(direct, ctx, list):
    myList = list
    if direct == "enter":
        # Reinitialise objects
        nodes = {}
        vals = {}
        pars = []
        varis = []
        consts = []
        addVar("__TEMP__")  # Special variable for calculations
        pass
    elif direct == "exit":
        # THIS IS WHERE THE WHOLE PROGRAM IS GONNA BE BUILT?
        pass
    return myList


def m(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass
    return myList


def f(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        # Declare memory for vars and consts

        myData = nodes[ctx]

        if myData[2] == "":
            pass

    return myList


def p(direct, ctx, list):
    myList = list
    if direct == "enter":
        inP = True
        pass
    elif direct == "exit":
        inP = False
        pass
    return myList


def l(direct, ctx, list):
    myList = list
    if direct == "enter":
        if inP:
            addPar(ctx.start.text)
        elif inD:
            addVar(ctx.start.text)
    elif direct == "exit":
        pass
    return myList


def d(direct, ctx, list):
    myList = list
    if direct == "enter":
        inD = True
        pass
    elif direct == "exit":
        inD = False
        pass


def s(direct, ctx, list):
    myList = list
    if direct == "enter":
        # Need to find out which branch to follow
        text = ctx.start.text
        if text == "if":
            myList.append(getDependencies(2))
            myList.append("if")
        elif text == "while":
            myList.append(getDependencies(2))
            myList.append("while")
        else:  # text == ident
            pass

    elif direct == "exit":
        myData = nodes[ctx]

        # WHILE AND IF NEED TO REPLACE <TRUE> AND <FALSE> IN C TEMPLATE

        if myData[2] == "if":
            template = getFileAsString("t_if.asm")
            template.replace("<template>", "")
            template.replace("<NUM>", "")

        elif myData[2] == "while":
            template = getFileAsString("t_while.asm")
            template.replace("<template>", "")
            template.replace("<NUM>", "")
            template.replace("<loop-body>")
        elif myData[2] == "s":
            pass
        elif myData[2] == "ident":
            template = getFileAsString("")
        elif myData[2] == "ep":
            pass  # Do we actually do nothing in this instance?
    return myList


def r(direct, ctx, list):
    myList = list
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
        template = getFileAsString("t_address_con.asm")
        template.replace("<X>", value)
        template.replace("<destreg>", "%" + register)
        return template
    elif value in varis:  # Variable
        template = getFileAsString("t_address_var.asm")
        template.replace("<N>", str(varis.indexOf(value) + 1))
        template.replace("<destreg>", "%" + register)
        return template
    elif value in pars:  # Parameter
        template = getFileAsString("t_address_vec.asm")
        template.replace("<argreg-N+1>",
                         "%" + registers[pars.indexOf(value) + 1])
        template.replace("<destreg>", "%" + register)
        return template


def e(direct, ctx, list):
    myList = list
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

        if len(myData[1]) == 2:
            if vals[myData[1][1]] is list:
                dep2 = vals[myData[1][1]][0]
                tem2 = vals[myData[1][1]][1]
            else:
                dep2 = vals[myData[1][1]]

        template = None
        if myData[2] == "op":
            template = getFileAsString("t_ident_=_op(factor,_factor).asm")
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
            template = getFileAsString("t_ident_=_factor.asm")
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
        tempVal = myData.pop(0)
        myData.insert(0, [])
        myData[0].append(tempVal)
        myData[0].append(template)

        myList = myData

    return myList


def c(direct, ctx, list):
    myList = list
    if direct == "enter":
        myList.append(getDependencies(2))
        if "<" in ctx.getText():
            myList.append("less")
        elif ">" in ctx.getText():
            myList.append("greater")
    elif direct == "exit":

        dep = None
        tem = None

        if vals[myList[1][0]] is list:
            dep = vals[myList[1][0]][0]
            tem = vals[myList[1][0]][1]
        else:
            dep = vals[myList[1][0]]

        template = getFileAsString("t_sum.asm")
        template.replace("<load-source-rax>", load(dep, "rax"))
        template.replace("<X>", str(getVal()))
        template.replace("<NUMBER>", vals[myList[1][1]])
        if dep.isnumeric():
            template.replace("addq    $16,    " + "%" + "rax", "")

        # Concaternate templates
        if tem is not None:
            template = tem + template

        # Change list[0] to list, 0 = depVal, 1 = assembly template
        tempVal = myList.pop(0)
        myList.insert(0, [])
        myList[0].append(tempVal)
        myList[0].append(template)

    return myList


def ident(direct, ctx, list):
    myList = list
    if direct == "enter":
        myList.append(getDependencies(0))
        myList.append(ctx.start.text)
    elif direct == "exit":
        # Defer finding out par vs var for later
        #  I still need the text at this point
        vals[myList[0]] = myList[2]
    return myList


def num(direct, ctx, list):
    myList = list
    if direct == "enter":
        myList.append(getDependencies(0))
        myList.append(ctx.start.text)
        addConst(myList[2])
    elif direct == "exit":
        if myList[2] in consts:
            vals[myList[0]] = myList[2]
    return myList
