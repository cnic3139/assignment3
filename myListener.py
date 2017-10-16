import sys
from build.VPLListener import VPLListener
from build.VPLParser import VPLParser


class myListener(VPLListener):

    # Enter a parse tree produced by VPLParser#start.
    def enterStart(self, ctx: VPLParser.StartContext):
        print("Entering start!")

    # Exit a parse tree produced by VPLParser#start.
    def exitStart(self, ctx: VPLParser.StartContext):
        print("Exiting start!")

    # Enter a parse tree produced by VPLParser#m.
    def enterM(self, ctx: VPLParser.MContext):
        print("Entering m!")

    # Exit a parse tree produced by VPLParser#m.
    def exitM(self, ctx: VPLParser.MContext):
        print("Exiting m!")

    # Enter a parse tree produced by VPLParser#f.
    def enterF(self, ctx: VPLParser.FContext):
        print("Entering f!")

    # Exit a parse tree produced by VPLParser#f.
    def exitF(self, ctx: VPLParser.FContext):
        print("Exiting f!")

    # Enter a parse tree produced by VPLParser#p.
    def enterP(self, ctx: VPLParser.PContext):
        print("Entering p!")

    # Exit a parse tree produced by VPLParser#p.
    def exitP(self, ctx: VPLParser.PContext):
        print("Exiting!p")

    # Enter a parse tree produced by VPLParser#l.
    def enterL(self, ctx: VPLParser.LContext):
        print("Entering l!")

    # Exit a parse tree produced by VPLParser#l.
    def exitL(self, ctx: VPLParser.LContext):
        print("Exiting l!")

    # Enter a parse tree produced by VPLParser#d.
    def enterD(self, ctx: VPLParser.DContext):
        print("Entering d!")

    # Exit a parse tree produced by VPLParser#d.
    def exitD(self, ctx: VPLParser.DContext):
        print("Exiting d !")

    # Enter a parse tree produced by VPLParser#s.
    def enterS(self, ctx: VPLParser.SContext):
        print("Entering s!")

    # Exit a parse tree produced by VPLParser#s.
    def exitS(self, ctx: VPLParser.SContext):
        print("Exiting s !")

    # Enter a parse tree produced by VPLParser#r.
    def enterR(self, ctx: VPLParser.RContext):
        print("Entering r!")

    # Exit a parse tree produced by VPLParser#r.
    def exitR(self, ctx: VPLParser.RContext):
        print("Exiting r !")

    # Enter a parse tree produced by VPLParser#e.
    def enterE(self, ctx: VPLParser.EContext):
        print("Entering e!")

    # Exit a parse tree produced by VPLParser#e.
    def exitE(self, ctx: VPLParser.EContext):
        print("Exiting e !")

    # Enter a parse tree produced by VPLParser#c.
    def enterC(self, ctx: VPLParser.CContext):
        print("Entering c!")

    # Exit a parse tree produced by VPLParser#c.
    def exitC(self, ctx: VPLParser.CContext):
        print("Exiting c !")
