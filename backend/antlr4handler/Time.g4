grammar Time;
prog: stat ;
stat: expr # printExpr
      ;
expr: INT ':' INT# HourMinute
      ;
INT : [0-9]+ ;
WS: [ \t\n\r]+ ->skip;