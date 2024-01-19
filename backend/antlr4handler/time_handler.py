# =================================
# File : time_handler.py
# Description : 这里是时间解析器
# Author : QinLing
# CREATE TIME : 2024/1/16 13:42
# =================================
from antlr4 import *
from .TimeVisitor import TimeVisitor
from .TimeParser import TimeParser
from .TimeLexer import TimeLexer
class TimeHandlerVisitor(TimeVisitor):
    def visitPrintExpr(self, ctx:TimeParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitHourMinute(self, ctx:TimeParser.HourMinuteContext):
        hour = int(ctx.INT(0).getText())
        minute = int(ctx.INT(1).getText())

        return [hour,minute]

def handler(time):
    input_stream = InputStream(time)
    lexer = TimeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TimeParser(stream)
    tree = parser.expr()
    visitor = TimeHandlerVisitor()
    return visitor.visit(tree)

if __name__ == "__main__" :
    time = input()
    print(handler(time))