import sys
from build.VPLListener import VPLListener
from build.VPLParser import VPLParser


class myListener(VPLListener):

    def __init__(self, funName):
        self.functionName = funName

    # Enter a parse tree produced by VPLParser#start.
    def enterStart(self, ctx: VPLParser.StartContext):
        print("Entering start!", dir(ctx), ctx.getText())
        self.functionName("start", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#start.
    def exitStart(self, ctx: VPLParser.StartContext):
        print("Exiting start!", ctx)
        self.functionName("start", "", ctx.getText())

    # Enter a parse tree produced by VPLParser#m.
    def enterM(self, ctx: VPLParser.MContext):
        print("Entering m!", ctx, ctx.getText())
        self.functionName("m", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#m.
    def exitM(self, ctx: VPLParser.MContext):
        print("Exiting m!", ctx)
        self.functionName("m", "exit", ctx.getText())

    # Enter a parse tree produced by VPLParser#f.
    def enterF(self, ctx: VPLParser.FContext):
        print("Entering f!", ctx, ctx.getText())
        self.functionName("f", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#f.
    def exitF(self, ctx: VPLParser.FContext):
        print("Exiting f!", ctx)
        self.functionName("f", "exit", ctx.getText())

    # Enter a parse tree produced by VPLParser#p.
    def enterP(self, ctx: VPLParser.PContext):
        print("Entering p!", ctx, ctx.getText())
        self.functionName("p", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#p.
    def exitP(self, ctx: VPLParser.PContext):
        print("Exiting p!", ctx)
        self.functionName("p", "exit", ctx.getText())

    # Enter a parse tree produced by VPLParser#l.
    def enterL(self, ctx: VPLParser.LContext):
        print("Entering l!", ctx, ctx.getText())
        self.functionName("l", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#l.
    def exitL(self, ctx: VPLParser.LContext):
        print("Exiting l!", ctx)
        self.functionName("l", "exit", ctx.getText())

    # Enter a parse tree produced by VPLParser#d.
    def enterD(self, ctx: VPLParser.DContext):
        print("Entering d!", ctx)
        self.functionName("d", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#d.
    def exitD(self, ctx: VPLParser.DContext):
        print("Exiting d!", ctx)
        self.functionName("d", "exit", ctx.getText())

    # Enter a parse tree produced by VPLParser#s.
    def enterS(self, ctx: VPLParser.SContext):
        print("Entering s!", ctx, ctx.getText())
        self.functionName("s", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#s.
    def exitS(self, ctx: VPLParser.SContext):
        print("Exiting s!", ctx)
        self.functionName("s", "exit", ctx.getText())

    # Enter a parse tree produced by VPLParser#r.
    def enterR(self, ctx: VPLParser.RContext):
        print("Entering r!", ctx)
        self.functionName("r", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#r.
    def exitR(self, ctx: VPLParser.RContext):
        print("Exiting r!", ctx)
        self.functionName("r", "exit", ctx.getText())

    # Enter a parse tree produced by VPLParser#e.
    def enterE(self, ctx: VPLParser.EContext):
        print("Entering e!", ctx)
        self.functionName("e", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#e.
    def exitE(self, ctx: VPLParser.EContext):
        print("Exiting e!", ctx)
        self.functionName("e", "exit", ctx.getText())

    # Enter a parse tree produced by VPLParser#c.
    def enterC(self, ctx: VPLParser.CContext):
        print("Entering c!", ctx)
        self.functionName("c", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#c.
    def exitC(self, ctx: VPLParser.CContext):
        print("Exiting c!", ctx)
        self.functionName("c", "exit", ctx.getText())

    # Enter a parse tree produced by VPLParser#ident.
    def enterIdent(self, ctx: VPLParser.IdentContext):
        print("Entering ident!", ctx)
        self.functionName("ident", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#ident.
    def exitIdent(self, ctx: VPLParser.IdentContext):
        print("Exiting ident!", ctx)
        self.functionName("ident", "exit", ctx.getText())

    # Enter a parse tree produced by VPLParser#num.
    def enterNum(self, ctx: VPLParser.NumContext):
        print("Entering num!", ctx)
        self.functionName("num", "enter", ctx.getText())

    # Exit a parse tree produced by VPLParser#num.
    def exitNum(self, ctx: VPLParser.NumContext):
        print("Exiting num!", ctx)
        self.functionName("num", "exit", ctx.getText())
