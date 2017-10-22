import sys
from build.VPLListener import VPLListener
from build.VPLParser import VPLParser


class myListener(VPLListener):

    def __init__(self, funName):
        self.functionName = funName

    # Enter a parse tree produced by VPLParser#start.
    def enterStart(self, ctx: VPLParser.StartContext):
        print("ctx:", dir(ctx))
        print("Entering start!", ctx.start.text)
        print("PARENT", ctx.parentCtx)
        self.functionName("start", "enter", ctx)

    # Exit a parse tree produced by VPLParser#start.
    def exitStart(self, ctx: VPLParser.StartContext):
        print("Exiting start!", ctx)
        self.functionName("start", "", ctx)

    # Enter a parse tree produced by VPLParser#m.
    def enterM(self, ctx: VPLParser.MContext):
        print("Entering m!", ctx.start.text)
        self.functionName("m", "enter", ctx)

    # Exit a parse tree produced by VPLParser#m.
    def exitM(self, ctx: VPLParser.MContext):
        print("Exiting m!", ctx)
        self.functionName("m", "exit", ctx)

    # Enter a parse tree produced by VPLParser#f.
    def enterF(self, ctx: VPLParser.FContext):
        print("Entering f!", ctx.start.text)
        print("PARENT:", ctx.parentCtx)
        self.functionName("f", "enter", ctx)

    # Exit a parse tree produced by VPLParser#f.
    def exitF(self, ctx: VPLParser.FContext):
        print("Exiting f!", ctx)
        self.functionName("f", "exit", ctx)

    # Enter a parse tree produced by VPLParser#p.
    def enterP(self, ctx: VPLParser.PContext):
        print("Entering p!", ctx.start.text)
        self.functionName("p", "enter", ctx)

    # Exit a parse tree produced by VPLParser#p.
    def exitP(self, ctx: VPLParser.PContext):
        print("Exiting p!", ctx)
        self.functionName("p", "exit", ctx)

    # Enter a parse tree produced by VPLParser#l.
    def enterL(self, ctx: VPLParser.LContext):
        print("Entering l!", ctx.start.text)
        self.functionName("l", "enter", ctx)

    # Exit a parse tree produced by VPLParser#l.
    def exitL(self, ctx: VPLParser.LContext):
        print("Exiting l!", ctx)
        self.functionName("l", "exit", ctx)

    # Enter a parse tree produced by VPLParser#d.
    def enterD(self, ctx: VPLParser.DContext):
        print("Entering d!", ctx.start.text)
        self.functionName("d", "enter", ctx)

    # Exit a parse tree produced by VPLParser#d.
    def exitD(self, ctx: VPLParser.DContext):
        print("Exiting d!", ctx)
        self.functionName("d", "exit", ctx)

    # Enter a parse tree produced by VPLParser#s.
    def enterS(self, ctx: VPLParser.SContext):
        print("Entering s!", ctx.start.text)
        print("CHILDREN:", ctx.getText())
        self.functionName("s", "enter", ctx)

    # Exit a parse tree produced by VPLParser#s.
    def exitS(self, ctx: VPLParser.SContext):
        print("Exiting s!", ctx)
        self.functionName("s", "exit", ctx)

    # Enter a parse tree produced by VPLParser#r.
    def enterR(self, ctx: VPLParser.RContext):
        print("Entering r!", ctx.start.text)
        self.functionName("r", "enter", ctx)

    # Exit a parse tree produced by VPLParser#r.
    def exitR(self, ctx: VPLParser.RContext):
        print("Exiting r!", ctx)
        self.functionName("r", "exit", ctx)

    # Enter a parse tree produced by VPLParser#e.
    def enterE(self, ctx: VPLParser.EContext):
        print("Entering e!", ctx.start.text)
        self.functionName("e", "enter", ctx)

    # Exit a parse tree produced by VPLParser#e.
    def exitE(self, ctx: VPLParser.EContext):
        print("Exiting e!", ctx)
        self.functionName("e", "exit", ctx)

    # Enter a parse tree produced by VPLParser#c.
    def enterC(self, ctx: VPLParser.CContext):
        print("Entering c!", ctx.getText())
        self.functionName("c", "enter", ctx)

    # Exit a parse tree produced by VPLParser#c.
    def exitC(self, ctx: VPLParser.CContext):
        print("Exiting c!", ctx)
        self.functionName("c", "exit", ctx)

    # Enter a parse tree produced by VPLParser#ident.
    def enterIdent(self, ctx: VPLParser.IdentContext):
        print("Entering ident!", ctx.start.text)
        self.functionName("ident", "enter", ctx)

    # Exit a parse tree produced by VPLParser#ident.
    def exitIdent(self, ctx: VPLParser.IdentContext):
        print("Exiting ident!", ctx)
        self.functionName("ident", "exit", ctx)

    # Enter a parse tree produced by VPLParser#num.
    def enterNum(self, ctx: VPLParser.NumContext):
        print("Entering num!", ctx.start.text)
        self.functionName("num", "enter", ctx)

    # Exit a parse tree produced by VPLParser#num.
    def exitNum(self, ctx: VPLParser.NumContext):
        print("Exiting num!", ctx)
        self.functionName("num", "exit", ctx)
