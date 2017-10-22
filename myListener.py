import sys
from build.VPLListener import VPLListener
from build.VPLParser import VPLParser


class myListener(VPLListener):

    def __init__(self, funName):
        self.functionName = funName

    # Enter a parse tree produced by VPLParser#start.
    def enterStart(self, ctx: VPLParser.StartContext):
        self.functionName("start", "enter", ctx)

    # Exit a parse tree produced by VPLParser#start.
    def exitStart(self, ctx: VPLParser.StartContext):
        self.functionName("start", "exit", ctx)

    # Enter a parse tree produced by VPLParser#m.
    def enterM(self, ctx: VPLParser.MContext):
        self.functionName("m", "enter", ctx)

    # Exit a parse tree produced by VPLParser#m.
    def exitM(self, ctx: VPLParser.MContext):
        self.functionName("m", "exit", ctx)

    # Enter a parse tree produced by VPLParser#f.
    def enterF(self, ctx: VPLParser.FContext):
        self.functionName("f", "enter", ctx)

    # Exit a parse tree produced by VPLParser#f.
    def exitF(self, ctx: VPLParser.FContext):
        self.functionName("f", "exit", ctx)

    # Enter a parse tree produced by VPLParser#p.
    def enterP(self, ctx: VPLParser.PContext):
        self.functionName("p", "enter", ctx)

    # Exit a parse tree produced by VPLParser#p.
    def exitP(self, ctx: VPLParser.PContext):
        self.functionName("p", "exit", ctx)

    # Enter a parse tree produced by VPLParser#l.
    def enterL(self, ctx: VPLParser.LContext):
        self.functionName("l", "enter", ctx)

    # Exit a parse tree produced by VPLParser#l.
    def exitL(self, ctx: VPLParser.LContext):
        self.functionName("l", "exit", ctx)

    # Enter a parse tree produced by VPLParser#d.
    def enterD(self, ctx: VPLParser.DContext):
        self.functionName("d", "enter", ctx)

    # Exit a parse tree produced by VPLParser#d.
    def exitD(self, ctx: VPLParser.DContext):
        self.functionName("d", "exit", ctx)

    # Enter a parse tree produced by VPLParser#s.
    def enterS(self, ctx: VPLParser.SContext):
        self.functionName("s", "enter", ctx)

    # Exit a parse tree produced by VPLParser#s.
    def exitS(self, ctx: VPLParser.SContext):
        self.functionName("s", "exit", ctx)

    # Enter a parse tree produced by VPLParser#r.
    def enterR(self, ctx: VPLParser.RContext):
        self.functionName("r", "enter", ctx)

    # Exit a parse tree produced by VPLParser#r.
    def exitR(self, ctx: VPLParser.RContext):
        self.functionName("r", "exit", ctx)

    # Enter a parse tree produced by VPLParser#e.
    def enterE(self, ctx: VPLParser.EContext):
        self.functionName("e", "enter", ctx)

    # Exit a parse tree produced by VPLParser#e.
    def exitE(self, ctx: VPLParser.EContext):
        self.functionName("e", "exit", ctx)

    # Enter a parse tree produced by VPLParser#c.
    def enterC(self, ctx: VPLParser.CContext):
        self.functionName("c", "enter", ctx)

    # Exit a parse tree produced by VPLParser#c.
    def exitC(self, ctx: VPLParser.CContext):
        self.functionName("c", "exit", ctx)

    # Enter a parse tree produced by VPLParser#ident.
    def enterIdent(self, ctx: VPLParser.IdentContext):
        self.functionName("ident", "enter", ctx)

    # Exit a parse tree produced by VPLParser#ident.
    def exitIdent(self, ctx: VPLParser.IdentContext):
        self.functionName("ident", "exit", ctx)

    # Enter a parse tree produced by VPLParser#num.
    def enterNum(self, ctx: VPLParser.NumContext):
        self.functionName("num", "enter", ctx)

    # Exit a parse tree produced by VPLParser#num.
    def exitNum(self, ctx: VPLParser.NumContext):
        self.functionName("num", "exit", ctx)
