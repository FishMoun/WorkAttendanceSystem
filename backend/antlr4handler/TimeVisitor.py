# Generated from Time.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .TimeParser import TimeParser
else:
    from TimeParser import TimeParser


# This class defines a complete generic visitor for a parse tree produced by TimeParser.

class TimeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TimeParser#prog.
    def visitProg(self, ctx: TimeParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TimeParser#printExpr.
    def visitPrintExpr(self, ctx: TimeParser.PrintExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TimeParser#HourMinute.
    def visitHourMinute(self, ctx: TimeParser.HourMinuteContext):
        return self.visitChildren(ctx)


del TimeParser
