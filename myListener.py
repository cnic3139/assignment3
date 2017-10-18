import sys
from build.VPLListener import VPLListener
from build.VPLParser import VPLParser


class myListener(VPLListener):

    def __init__(self, funName):
        self.functionName = funName

    # Enter a parse tree produced by VPLParser#start.
    def enterStart(self, ctx: VPLParser.StartContext):
        print("Entering start!")
        self.functionName("start", "enter")

    # Exit a parse tree produced by VPLParser#start.
    def exitStart(self, ctx: VPLParser.StartContext):
        print("Exiting start!")
        self.functionName("start", "")

    # Enter a parse tree produced by VPLParser#m.
    def enterM(self, ctx: VPLParser.MContext):
        print("Entering m!")
        self.functionName("m", "enter")

    # Exit a parse tree produced by VPLParser#m.
    def exitM(self, ctx: VPLParser.MContext):
        print("Exiting m!")
        self.functionName("m", "exit")

    # Enter a parse tree produced by VPLParser#f.
    def enterF(self, ctx: VPLParser.FContext):
        print("Entering f!")
        self.functionName("f", "enter")

    # Exit a parse tree produced by VPLParser#f.
    def exitF(self, ctx: VPLParser.FContext):
        print("Exiting f!")
        self.functionName("f", "exit")

    # Enter a parse tree produced by VPLParser#p.
    def enterP(self, ctx: VPLParser.PContext):
        print("Entering p!")
        self.functionName("p", "enter")

    # Exit a parse tree produced by VPLParser#p.
    def exitP(self, ctx: VPLParser.PContext):
        print("Exiting!p")
        self.functionName("p", "exit")

    # Enter a parse tree produced by VPLParser#l.
    def enterL(self, ctx: VPLParser.LContext):
        print("Entering l!")
        self.functionName("l", "enter")

    # Exit a parse tree produced by VPLParser#l.
    def exitL(self, ctx: VPLParser.LContext):
        print("Exiting l!")
        self.functionName("l", "exit")

    # Enter a parse tree produced by VPLParser#d.
    def enterD(self, ctx: VPLParser.DContext):
        print("Entering d!")
        self.functionName("d", "enter")

    # Exit a parse tree produced by VPLParser#d.
    def exitD(self, ctx: VPLParser.DContext):
        print("Exiting d !")
        self.functionName("d", "exit")

    # Enter a parse tree produced by VPLParser#s.
    def enterS(self, ctx: VPLParser.SContext):
        print("Entering s!")
        self.functionName("s", "enter")

    # Exit a parse tree produced by VPLParser#s.
    def exitS(self, ctx: VPLParser.SContext):
        print("Exiting s !")
        self.functionName("s", "exit")

    # Enter a parse tree produced by VPLParser#r.
    def enterR(self, ctx: VPLParser.RContext):
        print("Entering r!")
        self.functionName("r", "enter")

    # Exit a parse tree produced by VPLParser#r.
    def exitR(self, ctx: VPLParser.RContext):
        print("Exiting r !")
        self.functionName("r", "exit")

    # Enter a parse tree produced by VPLParser#e.
    def enterE(self, ctx: VPLParser.EContext):
        print("Entering e!")
        self.functionName("e", "enter")

    # Exit a parse tree produced by VPLParser#e.
    def exitE(self, ctx: VPLParser.EContext):
        print("Exiting e !")
        self.functionName("e", "exit")

    # Enter a parse tree produced by VPLParser#c.
    def enterC(self, ctx: VPLParser.CContext):
        print("Entering c!")
        self.functionName("c", "enter")

    # Exit a parse tree produced by VPLParser#c.
    def exitC(self, ctx: VPLParser.CContext):
        print("Exiting c !")
        self.functionName("c", "exit")
