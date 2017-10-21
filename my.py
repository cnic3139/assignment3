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


def getVal():
    global v
    returnVal = valCounter
    valCounter += 1
    return returnVal


def dispatcher(node, direct, ctx):

    if direct == "enter":
        enter(node, ctx)
    elif direct == "exit":
        exit(node, ctx)

    if node == "start":
        start(direct, ctx)
    elif node == "m":
        m()
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
    myList = []
    # This is where you will store your value
    # Try and get it from parent or make it yourself
    parentDeps = nodes[ctx.parentCtx][1]
    myNum = None
    for dep in parentDeps:
        if vals[dep] is None:
            myNum = dep
            break
    if myNum is None:
        myNum = getVal()
    myList.append(myNum)  # myList[0] is where value is located
    vals[myList[-1]] = None

    # TODO ====================================================================
    # So now we have our stuff filled, but our deps and formula will depend
    #  on the particular node, so use the selector to defer to nodes
    # TODO ====================================================================
    mylist = selector(node, "enter", ctx, mylist)

    # Store this list in nodes with ctx as key
    nodes[ctx] = myList


def exit(node, ctx):
    myData = nodes[ctx]

    myVal = myData[0]

    myDeps = myData[1]

    myCalc = myData[2]

    # USE formula in myCalc with vars in myDeps to put val in myVal


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
        pass
    elif direct == "exit":
        # THIS IS WHERE THE WHOLE PROGRAM IS GONNA BE BUILT?
        pass
    return mylist


def m(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass
    return mylist


def f(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass
    return mylist


def p(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass
    return mylist


def l(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass
    return mylist


def d(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass


def s(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass
    return mylist


def r(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass
    return mylist


def e(direct, ctx, list):
    myList = list
    if direct == "enter":
        

        # This is where you will store your dependencies
        myList.append([])  # myList[1] is list of where dependencies are
        myList[-1].append(getVal())
        vals[myList[-1][-1]] = None
        myList[-1].append(getVal())
        vals[myList[-1][-1]] = None
        myList.append(lambda x, y: x + y)  # myList[2] is how to calc value

        

    elif direct == "exit":
        # Lookup in node, get data from when you entered this node
        myData = nodes[ctx]

        # Now we should have all dependents accounted for, and we can
        #  get the value of this node and put it in the right place.

        # Now i have all my dependents set, i can write my stuff

    return mylist



def c(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass
    return mylist


def ident(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass
    return mylist


def num(direct, ctx, list):
    myList = list
    if direct == "enter":
        pass
    elif direct == "exit":
        pass
    return mylist