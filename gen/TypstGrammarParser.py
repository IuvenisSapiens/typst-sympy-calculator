# Generated from TypstGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,333,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,79,8,1,10,1,12,
        1,82,9,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,92,8,3,10,3,12,3,95,
        9,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,103,8,4,10,4,12,4,106,9,4,1,5,1,
        5,1,5,4,5,111,8,5,11,5,12,5,112,3,5,115,8,5,1,6,1,6,1,6,1,6,1,6,
        1,6,3,6,123,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,131,8,7,1,8,1,8,1,8,
        1,8,1,8,1,8,3,8,139,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,147,8,9,1,10,
        1,10,1,10,1,10,1,10,3,10,154,8,10,1,10,1,10,3,10,158,8,10,1,11,1,
        11,1,11,1,11,1,11,3,11,165,8,11,1,11,1,11,3,11,169,8,11,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,3,12,179,8,12,1,13,1,13,1,13,1,14,
        1,14,1,15,1,15,1,15,3,15,189,8,15,1,16,1,16,5,16,193,8,16,10,16,
        12,16,196,9,16,1,17,1,17,3,17,200,8,17,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,3,18,211,8,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,3,19,225,8,19,1,20,1,20,1,20,1,20,
        1,21,1,21,1,21,5,21,234,8,21,10,21,12,21,237,9,21,1,21,1,21,3,21,
        241,8,21,1,22,1,22,1,22,5,22,246,8,22,10,22,12,22,249,9,22,1,22,
        1,22,3,22,253,8,22,1,23,1,23,3,23,257,8,23,1,23,3,23,260,8,23,1,
        23,1,23,1,23,1,23,1,23,3,23,267,8,23,1,24,1,24,1,24,1,24,1,24,1,
        25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        27,1,27,3,27,289,8,27,1,27,1,27,1,27,1,27,1,27,3,27,296,8,27,1,28,
        1,28,3,28,300,8,28,1,28,1,28,1,28,1,28,1,29,1,29,5,29,308,8,29,10,
        29,12,29,311,9,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,
        31,3,31,323,8,31,1,32,1,32,3,32,327,8,32,1,33,1,33,3,33,331,8,33,
        1,33,1,309,3,2,6,8,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,0,1,1,0,1,
        4,343,0,68,1,0,0,0,2,72,1,0,0,0,4,83,1,0,0,0,6,85,1,0,0,0,8,96,1,
        0,0,0,10,114,1,0,0,0,12,116,1,0,0,0,14,124,1,0,0,0,16,132,1,0,0,
        0,18,146,1,0,0,0,20,148,1,0,0,0,22,159,1,0,0,0,24,178,1,0,0,0,26,
        180,1,0,0,0,28,183,1,0,0,0,30,188,1,0,0,0,32,190,1,0,0,0,34,197,
        1,0,0,0,36,210,1,0,0,0,38,224,1,0,0,0,40,226,1,0,0,0,42,235,1,0,
        0,0,44,247,1,0,0,0,46,254,1,0,0,0,48,268,1,0,0,0,50,273,1,0,0,0,
        52,277,1,0,0,0,54,286,1,0,0,0,56,297,1,0,0,0,58,305,1,0,0,0,60,314,
        1,0,0,0,62,322,1,0,0,0,64,324,1,0,0,0,66,330,1,0,0,0,68,69,5,5,0,
        0,69,70,3,2,1,0,70,71,5,6,0,0,71,1,1,0,0,0,72,73,6,1,-1,0,73,74,
        3,4,2,0,74,80,1,0,0,0,75,76,10,2,0,0,76,77,5,24,0,0,77,79,3,2,1,
        3,78,75,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,3,1,
        0,0,0,82,80,1,0,0,0,83,84,3,6,3,0,84,5,1,0,0,0,85,86,6,3,-1,0,86,
        87,3,8,4,0,87,93,1,0,0,0,88,89,10,2,0,0,89,90,5,25,0,0,90,92,3,6,
        3,3,91,88,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,7,
        1,0,0,0,95,93,1,0,0,0,96,97,6,4,-1,0,97,98,3,10,5,0,98,104,1,0,0,
        0,99,100,10,2,0,0,100,101,5,26,0,0,101,103,3,8,4,3,102,99,1,0,0,
        0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,9,1,0,0,0,
        106,104,1,0,0,0,107,108,5,25,0,0,108,115,3,10,5,0,109,111,3,32,16,
        0,110,109,1,0,0,0,111,112,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,
        0,113,115,1,0,0,0,114,107,1,0,0,0,114,110,1,0,0,0,115,11,1,0,0,0,
        116,122,5,18,0,0,117,123,3,66,33,0,118,119,5,9,0,0,119,120,3,42,
        21,0,120,121,5,10,0,0,121,123,1,0,0,0,122,117,1,0,0,0,122,118,1,
        0,0,0,123,13,1,0,0,0,124,130,5,18,0,0,125,131,3,66,33,0,126,127,
        5,9,0,0,127,128,3,4,2,0,128,129,5,10,0,0,129,131,1,0,0,0,130,125,
        1,0,0,0,130,126,1,0,0,0,131,15,1,0,0,0,132,138,5,19,0,0,133,139,
        3,34,17,0,134,135,5,9,0,0,135,136,3,4,2,0,136,137,5,10,0,0,137,139,
        1,0,0,0,138,133,1,0,0,0,138,134,1,0,0,0,139,17,1,0,0,0,140,141,3,
        14,7,0,141,142,3,16,8,0,142,147,1,0,0,0,143,144,3,16,8,0,144,145,
        3,14,7,0,145,147,1,0,0,0,146,140,1,0,0,0,146,143,1,0,0,0,147,19,
        1,0,0,0,148,157,5,18,0,0,149,158,3,66,33,0,150,153,5,9,0,0,151,154,
        3,4,2,0,152,154,3,2,1,0,153,151,1,0,0,0,153,152,1,0,0,0,154,155,
        1,0,0,0,155,156,5,10,0,0,156,158,1,0,0,0,157,149,1,0,0,0,157,150,
        1,0,0,0,158,21,1,0,0,0,159,168,5,19,0,0,160,169,3,34,17,0,161,164,
        5,9,0,0,162,165,3,4,2,0,163,165,3,2,1,0,164,162,1,0,0,0,164,163,
        1,0,0,0,165,166,1,0,0,0,166,167,5,10,0,0,167,169,1,0,0,0,168,160,
        1,0,0,0,168,161,1,0,0,0,169,23,1,0,0,0,170,179,3,20,10,0,171,179,
        3,22,11,0,172,173,3,20,10,0,173,174,3,16,8,0,174,179,1,0,0,0,175,
        176,3,16,8,0,176,177,3,20,10,0,177,179,1,0,0,0,178,170,1,0,0,0,178,
        171,1,0,0,0,178,172,1,0,0,0,178,175,1,0,0,0,179,25,1,0,0,0,180,181,
        5,16,0,0,181,182,3,24,12,0,182,27,1,0,0,0,183,184,7,0,0,0,184,29,
        1,0,0,0,185,189,5,27,0,0,186,189,3,28,14,0,187,189,3,26,13,0,188,
        185,1,0,0,0,188,186,1,0,0,0,188,187,1,0,0,0,189,31,1,0,0,0,190,194,
        3,34,17,0,191,193,3,30,15,0,192,191,1,0,0,0,193,196,1,0,0,0,194,
        192,1,0,0,0,194,195,1,0,0,0,195,33,1,0,0,0,196,194,1,0,0,0,197,199,
        3,36,18,0,198,200,3,16,8,0,199,198,1,0,0,0,199,200,1,0,0,0,200,35,
        1,0,0,0,201,211,3,38,19,0,202,211,3,40,20,0,203,211,3,46,23,0,204,
        211,3,48,24,0,205,211,3,50,25,0,206,211,3,52,26,0,207,211,3,54,27,
        0,208,211,3,56,28,0,209,211,3,66,33,0,210,201,1,0,0,0,210,202,1,
        0,0,0,210,203,1,0,0,0,210,204,1,0,0,0,210,205,1,0,0,0,210,206,1,
        0,0,0,210,207,1,0,0,0,210,208,1,0,0,0,210,209,1,0,0,0,211,37,1,0,
        0,0,212,213,5,9,0,0,213,214,3,4,2,0,214,215,5,10,0,0,215,225,1,0,
        0,0,216,217,5,11,0,0,217,218,3,4,2,0,218,219,5,12,0,0,219,225,1,
        0,0,0,220,221,5,13,0,0,221,222,3,4,2,0,222,223,5,14,0,0,223,225,
        1,0,0,0,224,212,1,0,0,0,224,216,1,0,0,0,224,220,1,0,0,0,225,39,1,
        0,0,0,226,227,5,15,0,0,227,228,3,4,2,0,228,229,5,15,0,0,229,41,1,
        0,0,0,230,231,3,2,1,0,231,232,5,21,0,0,232,234,1,0,0,0,233,230,1,
        0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,238,1,
        0,0,0,237,235,1,0,0,0,238,240,3,2,1,0,239,241,5,21,0,0,240,239,1,
        0,0,0,240,241,1,0,0,0,241,43,1,0,0,0,242,243,3,42,21,0,243,244,5,
        20,0,0,244,246,1,0,0,0,245,242,1,0,0,0,246,249,1,0,0,0,247,245,1,
        0,0,0,247,248,1,0,0,0,248,250,1,0,0,0,249,247,1,0,0,0,250,252,3,
        42,21,0,251,253,5,20,0,0,252,251,1,0,0,0,252,253,1,0,0,0,253,45,
        1,0,0,0,254,256,5,30,0,0,255,257,3,12,6,0,256,255,1,0,0,0,256,257,
        1,0,0,0,257,259,1,0,0,0,258,260,3,16,8,0,259,258,1,0,0,0,259,260,
        1,0,0,0,260,266,1,0,0,0,261,262,5,9,0,0,262,263,3,42,21,0,263,264,
        5,10,0,0,264,267,1,0,0,0,265,267,3,8,4,0,266,261,1,0,0,0,266,265,
        1,0,0,0,267,47,1,0,0,0,268,269,5,31,0,0,269,270,5,9,0,0,270,271,
        3,44,22,0,271,272,5,10,0,0,272,49,1,0,0,0,273,274,5,29,0,0,274,275,
        3,24,12,0,275,276,3,8,4,0,276,51,1,0,0,0,277,278,5,32,0,0,278,279,
        5,18,0,0,279,280,5,9,0,0,280,281,3,64,32,0,281,282,5,23,0,0,282,
        283,3,4,2,0,283,284,5,10,0,0,284,285,3,6,3,0,285,53,1,0,0,0,286,
        288,5,33,0,0,287,289,3,14,7,0,288,287,1,0,0,0,288,289,1,0,0,0,289,
        295,1,0,0,0,290,291,5,9,0,0,291,292,3,4,2,0,292,293,5,10,0,0,293,
        296,1,0,0,0,294,296,3,8,4,0,295,290,1,0,0,0,295,294,1,0,0,0,296,
        55,1,0,0,0,297,299,5,34,0,0,298,300,3,18,9,0,299,298,1,0,0,0,299,
        300,1,0,0,0,300,301,1,0,0,0,301,302,3,6,3,0,302,303,5,35,0,0,303,
        304,3,64,32,0,304,57,1,0,0,0,305,309,5,17,0,0,306,308,9,0,0,0,307,
        306,1,0,0,0,308,311,1,0,0,0,309,310,1,0,0,0,309,307,1,0,0,0,310,
        312,1,0,0,0,311,309,1,0,0,0,312,313,5,17,0,0,313,59,1,0,0,0,314,
        315,5,28,0,0,315,316,5,9,0,0,316,317,3,4,2,0,317,318,5,10,0,0,318,
        61,1,0,0,0,319,323,5,37,0,0,320,323,3,58,29,0,321,323,3,60,30,0,
        322,319,1,0,0,0,322,320,1,0,0,0,322,321,1,0,0,0,323,63,1,0,0,0,324,
        326,3,62,31,0,325,327,3,12,6,0,326,325,1,0,0,0,326,327,1,0,0,0,327,
        65,1,0,0,0,328,331,5,38,0,0,329,331,3,64,32,0,330,328,1,0,0,0,330,
        329,1,0,0,0,331,67,1,0,0,0,33,80,93,104,112,114,122,130,138,146,
        153,157,164,168,178,188,194,199,210,224,235,240,247,252,256,259,
        266,288,295,299,309,322,326,330
    ]

class TypstGrammarParser ( Parser ):

    grammarFileName = "TypstGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^T'", "'^top'", "'^(T)'", "'^(top)'", 
                     "'<typst_math_start>'", "'<typst_math_end>'", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'|'", "<INVALID>", "'\"'", "'_'", "'^'", "';'", "','", 
                     "'.'", "'->'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'<typst_math_accent>'", "'<typst_math_reduce>'", 
                     "'<typst_math_func>'", "'<typst_math_mat>'", "'lim'", 
                     "'log'", "'integral'", "'dif'", "'diff'", "'<typst_math_symbol_base>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "MATH_START", "MATH_END", "WS", "USELESS_SIGN", 
                      "L_PAREN", "R_PAREN", "L_BRACE", "R_BRACE", "L_BRACKET", 
                      "R_BRACKET", "BAR", "EVAL_BAR", "QUOTE", "UNDERSCORE", 
                      "CARET", "SEMICOLON", "COMMA", "PERIOD", "LIM_APPROACH_SYM", 
                      "RELATION_OP", "ADDITIVE_OP", "MP_OP", "POSTFIX_OP", 
                      "ACCENT_OP", "REDUCE_OP", "FUNC", "FUNC_MAT", "FUNC_LIM", 
                      "FUNC_LOG", "FUNC_INTEGRAL", "DIF", "DIFF", "SYMBOL_BASE", 
                      "NUMBER", "ID" ]

    RULE_math = 0
    RULE_relation = 1
    RULE_expr = 2
    RULE_additive = 3
    RULE_mp = 4
    RULE_unary = 5
    RULE_subargs = 6
    RULE_subexpr = 7
    RULE_supexpr = 8
    RULE_subsupexpr = 9
    RULE_subassign = 10
    RULE_supassign = 11
    RULE_subsupassign = 12
    RULE_eval_at = 13
    RULE_transpose = 14
    RULE_postfix_op = 15
    RULE_postfix = 16
    RULE_exp = 17
    RULE_comp = 18
    RULE_group = 19
    RULE_abs_group = 20
    RULE_args = 21
    RULE_mat_args = 22
    RULE_func = 23
    RULE_matrix = 24
    RULE_reduceit = 25
    RULE_lim = 26
    RULE_log = 27
    RULE_integral = 28
    RULE_text = 29
    RULE_accent = 30
    RULE_symbol_base = 31
    RULE_symbol = 32
    RULE_atom = 33

    ruleNames =  [ "math", "relation", "expr", "additive", "mp", "unary", 
                   "subargs", "subexpr", "supexpr", "subsupexpr", "subassign", 
                   "supassign", "subsupassign", "eval_at", "transpose", 
                   "postfix_op", "postfix", "exp", "comp", "group", "abs_group", 
                   "args", "mat_args", "func", "matrix", "reduceit", "lim", 
                   "log", "integral", "text", "accent", "symbol_base", "symbol", 
                   "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    MATH_START=5
    MATH_END=6
    WS=7
    USELESS_SIGN=8
    L_PAREN=9
    R_PAREN=10
    L_BRACE=11
    R_BRACE=12
    L_BRACKET=13
    R_BRACKET=14
    BAR=15
    EVAL_BAR=16
    QUOTE=17
    UNDERSCORE=18
    CARET=19
    SEMICOLON=20
    COMMA=21
    PERIOD=22
    LIM_APPROACH_SYM=23
    RELATION_OP=24
    ADDITIVE_OP=25
    MP_OP=26
    POSTFIX_OP=27
    ACCENT_OP=28
    REDUCE_OP=29
    FUNC=30
    FUNC_MAT=31
    FUNC_LIM=32
    FUNC_LOG=33
    FUNC_INTEGRAL=34
    DIF=35
    DIFF=36
    SYMBOL_BASE=37
    NUMBER=38
    ID=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATH_START(self):
            return self.getToken(TypstGrammarParser.MATH_START, 0)

        def relation(self):
            return self.getTypedRuleContext(TypstGrammarParser.RelationContext,0)


        def MATH_END(self):
            return self.getToken(TypstGrammarParser.MATH_END, 0)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_math

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath" ):
                listener.enterMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath" ):
                listener.exitMath(self)




    def math(self):

        localctx = TypstGrammarParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_math)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(TypstGrammarParser.MATH_START)
            self.state = 69
            self.relation(0)
            self.state = 70
            self.match(TypstGrammarParser.MATH_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExprContext,0)


        def relation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypstGrammarParser.RelationContext)
            else:
                return self.getTypedRuleContext(TypstGrammarParser.RelationContext,i)


        def RELATION_OP(self):
            return self.getToken(TypstGrammarParser.RELATION_OP, 0)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)



    def relation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TypstGrammarParser.RelationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_relation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TypstGrammarParser.RelationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relation)
                    self.state = 75
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 76
                    self.match(TypstGrammarParser.RELATION_OP)
                    self.state = 77
                    self.relation(3) 
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self):
            return self.getTypedRuleContext(TypstGrammarParser.AdditiveContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = TypstGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.additive(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mp(self):
            return self.getTypedRuleContext(TypstGrammarParser.MpContext,0)


        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypstGrammarParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(TypstGrammarParser.AdditiveContext,i)


        def ADDITIVE_OP(self):
            return self.getToken(TypstGrammarParser.ADDITIVE_OP, 0)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_additive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)



    def additive(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TypstGrammarParser.AdditiveContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_additive, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.mp(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TypstGrammarParser.AdditiveContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                    self.state = 88
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 89
                    self.match(TypstGrammarParser.ADDITIVE_OP)
                    self.state = 90
                    self.additive(3) 
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(TypstGrammarParser.UnaryContext,0)


        def mp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypstGrammarParser.MpContext)
            else:
                return self.getTypedRuleContext(TypstGrammarParser.MpContext,i)


        def MP_OP(self):
            return self.getToken(TypstGrammarParser.MP_OP, 0)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_mp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMp" ):
                listener.enterMp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMp" ):
                listener.exitMp(self)



    def mp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TypstGrammarParser.MpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_mp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TypstGrammarParser.MpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mp)
                    self.state = 99
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 100
                    self.match(TypstGrammarParser.MP_OP)
                    self.state = 101
                    self.mp(3) 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADDITIVE_OP(self):
            return self.getToken(TypstGrammarParser.ADDITIVE_OP, 0)

        def unary(self):
            return self.getTypedRuleContext(TypstGrammarParser.UnaryContext,0)


        def postfix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypstGrammarParser.PostfixContext)
            else:
                return self.getTypedRuleContext(TypstGrammarParser.PostfixContext,i)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)




    def unary(self):

        localctx = TypstGrammarParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unary)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(TypstGrammarParser.ADDITIVE_OP)
                self.state = 108
                self.unary()
                pass
            elif token in [9, 11, 13, 15, 17, 28, 29, 30, 31, 32, 33, 34, 37, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 109
                        self.postfix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 112 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubargsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(TypstGrammarParser.UNDERSCORE, 0)

        def atom(self):
            return self.getTypedRuleContext(TypstGrammarParser.AtomContext,0)


        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def args(self):
            return self.getTypedRuleContext(TypstGrammarParser.ArgsContext,0)


        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_subargs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubargs" ):
                listener.enterSubargs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubargs" ):
                listener.exitSubargs(self)




    def subargs(self):

        localctx = TypstGrammarParser.SubargsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subargs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(TypstGrammarParser.UNDERSCORE)
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 28, 37, 38]:
                self.state = 117
                self.atom()
                pass
            elif token in [9]:
                self.state = 118
                self.match(TypstGrammarParser.L_PAREN)
                self.state = 119
                self.args()
                self.state = 120
                self.match(TypstGrammarParser.R_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(TypstGrammarParser.UNDERSCORE, 0)

        def atom(self):
            return self.getTypedRuleContext(TypstGrammarParser.AtomContext,0)


        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_subexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubexpr" ):
                listener.enterSubexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubexpr" ):
                listener.exitSubexpr(self)




    def subexpr(self):

        localctx = TypstGrammarParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(TypstGrammarParser.UNDERSCORE)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 28, 37, 38]:
                self.state = 125
                self.atom()
                pass
            elif token in [9]:
                self.state = 126
                self.match(TypstGrammarParser.L_PAREN)
                self.state = 127
                self.expr()
                self.state = 128
                self.match(TypstGrammarParser.R_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SupexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(TypstGrammarParser.CARET, 0)

        def exp(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExpContext,0)


        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_supexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSupexpr" ):
                listener.enterSupexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSupexpr" ):
                listener.exitSupexpr(self)




    def supexpr(self):

        localctx = TypstGrammarParser.SupexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(TypstGrammarParser.CARET)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 133
                self.exp()
                pass

            elif la_ == 2:
                self.state = 134
                self.match(TypstGrammarParser.L_PAREN)
                self.state = 135
                self.expr()
                self.state = 136
                self.match(TypstGrammarParser.R_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubsupexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subexpr(self):
            return self.getTypedRuleContext(TypstGrammarParser.SubexprContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(TypstGrammarParser.SupexprContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_subsupexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubsupexpr" ):
                listener.enterSubsupexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubsupexpr" ):
                listener.exitSubsupexpr(self)




    def subsupexpr(self):

        localctx = TypstGrammarParser.SubsupexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_subsupexpr)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.subexpr()
                self.state = 141
                self.supexpr()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.supexpr()
                self.state = 144
                self.subexpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(TypstGrammarParser.UNDERSCORE, 0)

        def atom(self):
            return self.getTypedRuleContext(TypstGrammarParser.AtomContext,0)


        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExprContext,0)


        def relation(self):
            return self.getTypedRuleContext(TypstGrammarParser.RelationContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_subassign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubassign" ):
                listener.enterSubassign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubassign" ):
                listener.exitSubassign(self)




    def subassign(self):

        localctx = TypstGrammarParser.SubassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_subassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(TypstGrammarParser.UNDERSCORE)
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 28, 37, 38]:
                self.state = 149
                self.atom()
                pass
            elif token in [9]:
                self.state = 150
                self.match(TypstGrammarParser.L_PAREN)
                self.state = 153
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 151
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 152
                    self.relation(0)
                    pass


                self.state = 155
                self.match(TypstGrammarParser.R_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SupassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(TypstGrammarParser.CARET, 0)

        def exp(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExpContext,0)


        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExprContext,0)


        def relation(self):
            return self.getTypedRuleContext(TypstGrammarParser.RelationContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_supassign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSupassign" ):
                listener.enterSupassign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSupassign" ):
                listener.exitSupassign(self)




    def supassign(self):

        localctx = TypstGrammarParser.SupassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_supassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(TypstGrammarParser.CARET)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 160
                self.exp()
                pass

            elif la_ == 2:
                self.state = 161
                self.match(TypstGrammarParser.L_PAREN)
                self.state = 164
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 162
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 163
                    self.relation(0)
                    pass


                self.state = 166
                self.match(TypstGrammarParser.R_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubsupassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subassign(self):
            return self.getTypedRuleContext(TypstGrammarParser.SubassignContext,0)


        def supassign(self):
            return self.getTypedRuleContext(TypstGrammarParser.SupassignContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(TypstGrammarParser.SupexprContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_subsupassign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubsupassign" ):
                listener.enterSubsupassign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubsupassign" ):
                listener.exitSubsupassign(self)




    def subsupassign(self):

        localctx = TypstGrammarParser.SubsupassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_subsupassign)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.subassign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.supassign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.subassign()
                self.state = 173
                self.supexpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.supexpr()
                self.state = 176
                self.subassign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eval_atContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVAL_BAR(self):
            return self.getToken(TypstGrammarParser.EVAL_BAR, 0)

        def subsupassign(self):
            return self.getTypedRuleContext(TypstGrammarParser.SubsupassignContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_eval_at

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEval_at" ):
                listener.enterEval_at(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEval_at" ):
                listener.exitEval_at(self)




    def eval_at(self):

        localctx = TypstGrammarParser.Eval_atContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_eval_at)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(TypstGrammarParser.EVAL_BAR)
            self.state = 181
            self.subsupassign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransposeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_transpose

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranspose" ):
                listener.enterTranspose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranspose" ):
                listener.exitTranspose(self)




    def transpose(self):

        localctx = TypstGrammarParser.TransposeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_transpose)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Postfix_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSTFIX_OP(self):
            return self.getToken(TypstGrammarParser.POSTFIX_OP, 0)

        def transpose(self):
            return self.getTypedRuleContext(TypstGrammarParser.TransposeContext,0)


        def eval_at(self):
            return self.getTypedRuleContext(TypstGrammarParser.Eval_atContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_postfix_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix_op" ):
                listener.enterPostfix_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix_op" ):
                listener.exitPostfix_op(self)




    def postfix_op(self):

        localctx = TypstGrammarParser.Postfix_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_postfix_op)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(TypstGrammarParser.POSTFIX_OP)
                pass
            elif token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.transpose()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.eval_at()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExpContext,0)


        def postfix_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypstGrammarParser.Postfix_opContext)
            else:
                return self.getTypedRuleContext(TypstGrammarParser.Postfix_opContext,i)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_postfix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix" ):
                listener.enterPostfix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix" ):
                listener.exitPostfix(self)




    def postfix(self):

        localctx = TypstGrammarParser.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_postfix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.exp()
            self.state = 194
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 191
                    self.postfix_op() 
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(TypstGrammarParser.CompContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(TypstGrammarParser.SupexprContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = TypstGrammarParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.comp()
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 198
                self.supexpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def group(self):
            return self.getTypedRuleContext(TypstGrammarParser.GroupContext,0)


        def abs_group(self):
            return self.getTypedRuleContext(TypstGrammarParser.Abs_groupContext,0)


        def func(self):
            return self.getTypedRuleContext(TypstGrammarParser.FuncContext,0)


        def matrix(self):
            return self.getTypedRuleContext(TypstGrammarParser.MatrixContext,0)


        def reduceit(self):
            return self.getTypedRuleContext(TypstGrammarParser.ReduceitContext,0)


        def lim(self):
            return self.getTypedRuleContext(TypstGrammarParser.LimContext,0)


        def log(self):
            return self.getTypedRuleContext(TypstGrammarParser.LogContext,0)


        def integral(self):
            return self.getTypedRuleContext(TypstGrammarParser.IntegralContext,0)


        def atom(self):
            return self.getTypedRuleContext(TypstGrammarParser.AtomContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)




    def comp(self):

        localctx = TypstGrammarParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comp)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 11, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.group()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.abs_group()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.func()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.matrix()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                self.reduceit()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 6)
                self.state = 206
                self.lim()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 7)
                self.state = 207
                self.log()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 8)
                self.state = 208
                self.integral()
                pass
            elif token in [17, 28, 37, 38]:
                self.enterOuterAlt(localctx, 9)
                self.state = 209
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def L_BRACE(self):
            return self.getToken(TypstGrammarParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(TypstGrammarParser.R_BRACE, 0)

        def L_BRACKET(self):
            return self.getToken(TypstGrammarParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(TypstGrammarParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)




    def group(self):

        localctx = TypstGrammarParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_group)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(TypstGrammarParser.L_PAREN)
                self.state = 213
                self.expr()
                self.state = 214
                self.match(TypstGrammarParser.R_PAREN)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(TypstGrammarParser.L_BRACE)
                self.state = 217
                self.expr()
                self.state = 218
                self.match(TypstGrammarParser.R_BRACE)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(TypstGrammarParser.L_BRACKET)
                self.state = 221
                self.expr()
                self.state = 222
                self.match(TypstGrammarParser.R_BRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Abs_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BAR(self, i:int=None):
            if i is None:
                return self.getTokens(TypstGrammarParser.BAR)
            else:
                return self.getToken(TypstGrammarParser.BAR, i)

        def expr(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_abs_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbs_group" ):
                listener.enterAbs_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbs_group" ):
                listener.exitAbs_group(self)




    def abs_group(self):

        localctx = TypstGrammarParser.Abs_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_abs_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(TypstGrammarParser.BAR)
            self.state = 227
            self.expr()
            self.state = 228
            self.match(TypstGrammarParser.BAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypstGrammarParser.RelationContext)
            else:
                return self.getTypedRuleContext(TypstGrammarParser.RelationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TypstGrammarParser.COMMA)
            else:
                return self.getToken(TypstGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = TypstGrammarParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 230
                    self.relation(0)
                    self.state = 231
                    self.match(TypstGrammarParser.COMMA) 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 238
            self.relation(0)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 239
                self.match(TypstGrammarParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mat_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def args(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypstGrammarParser.ArgsContext)
            else:
                return self.getTypedRuleContext(TypstGrammarParser.ArgsContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(TypstGrammarParser.SEMICOLON)
            else:
                return self.getToken(TypstGrammarParser.SEMICOLON, i)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_mat_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMat_args" ):
                listener.enterMat_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMat_args" ):
                listener.exitMat_args(self)




    def mat_args(self):

        localctx = TypstGrammarParser.Mat_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mat_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 242
                    self.args()
                    self.state = 243
                    self.match(TypstGrammarParser.SEMICOLON) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 250
            self.args()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 251
                self.match(TypstGrammarParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(TypstGrammarParser.FUNC, 0)

        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def args(self):
            return self.getTypedRuleContext(TypstGrammarParser.ArgsContext,0)


        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def mp(self):
            return self.getTypedRuleContext(TypstGrammarParser.MpContext,0)


        def subargs(self):
            return self.getTypedRuleContext(TypstGrammarParser.SubargsContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(TypstGrammarParser.SupexprContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = TypstGrammarParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(TypstGrammarParser.FUNC)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 255
                self.subargs()


            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 258
                self.supexpr()


            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 261
                self.match(TypstGrammarParser.L_PAREN)
                self.state = 262
                self.args()
                self.state = 263
                self.match(TypstGrammarParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 265
                self.mp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_MAT(self):
            return self.getToken(TypstGrammarParser.FUNC_MAT, 0)

        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def mat_args(self):
            return self.getTypedRuleContext(TypstGrammarParser.Mat_argsContext,0)


        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_matrix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix" ):
                listener.enterMatrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix" ):
                listener.exitMatrix(self)




    def matrix(self):

        localctx = TypstGrammarParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(TypstGrammarParser.FUNC_MAT)
            self.state = 269
            self.match(TypstGrammarParser.L_PAREN)
            self.state = 270
            self.mat_args()
            self.state = 271
            self.match(TypstGrammarParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReduceitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REDUCE_OP(self):
            return self.getToken(TypstGrammarParser.REDUCE_OP, 0)

        def subsupassign(self):
            return self.getTypedRuleContext(TypstGrammarParser.SubsupassignContext,0)


        def mp(self):
            return self.getTypedRuleContext(TypstGrammarParser.MpContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_reduceit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReduceit" ):
                listener.enterReduceit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReduceit" ):
                listener.exitReduceit(self)




    def reduceit(self):

        localctx = TypstGrammarParser.ReduceitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_reduceit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(TypstGrammarParser.REDUCE_OP)
            self.state = 274
            self.subsupassign()
            self.state = 275
            self.mp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_LIM(self):
            return self.getToken(TypstGrammarParser.FUNC_LIM, 0)

        def UNDERSCORE(self):
            return self.getToken(TypstGrammarParser.UNDERSCORE, 0)

        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def symbol(self):
            return self.getTypedRuleContext(TypstGrammarParser.SymbolContext,0)


        def LIM_APPROACH_SYM(self):
            return self.getToken(TypstGrammarParser.LIM_APPROACH_SYM, 0)

        def expr(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def additive(self):
            return self.getTypedRuleContext(TypstGrammarParser.AdditiveContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_lim

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLim" ):
                listener.enterLim(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLim" ):
                listener.exitLim(self)




    def lim(self):

        localctx = TypstGrammarParser.LimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(TypstGrammarParser.FUNC_LIM)
            self.state = 278
            self.match(TypstGrammarParser.UNDERSCORE)
            self.state = 279
            self.match(TypstGrammarParser.L_PAREN)
            self.state = 280
            self.symbol()
            self.state = 281
            self.match(TypstGrammarParser.LIM_APPROACH_SYM)
            self.state = 282
            self.expr()
            self.state = 283
            self.match(TypstGrammarParser.R_PAREN)
            self.state = 284
            self.additive(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_LOG(self):
            return self.getToken(TypstGrammarParser.FUNC_LOG, 0)

        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def mp(self):
            return self.getTypedRuleContext(TypstGrammarParser.MpContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(TypstGrammarParser.SubexprContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_log

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog" ):
                listener.enterLog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog" ):
                listener.exitLog(self)




    def log(self):

        localctx = TypstGrammarParser.LogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_log)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(TypstGrammarParser.FUNC_LOG)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 287
                self.subexpr()


            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 290
                self.match(TypstGrammarParser.L_PAREN)
                self.state = 291
                self.expr()
                self.state = 292
                self.match(TypstGrammarParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 294
                self.mp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_INTEGRAL(self):
            return self.getToken(TypstGrammarParser.FUNC_INTEGRAL, 0)

        def additive(self):
            return self.getTypedRuleContext(TypstGrammarParser.AdditiveContext,0)


        def DIF(self):
            return self.getToken(TypstGrammarParser.DIF, 0)

        def symbol(self):
            return self.getTypedRuleContext(TypstGrammarParser.SymbolContext,0)


        def subsupexpr(self):
            return self.getTypedRuleContext(TypstGrammarParser.SubsupexprContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_integral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegral" ):
                listener.enterIntegral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegral" ):
                listener.exitIntegral(self)




    def integral(self):

        localctx = TypstGrammarParser.IntegralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_integral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(TypstGrammarParser.FUNC_INTEGRAL)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18 or _la==19:
                self.state = 298
                self.subsupexpr()


            self.state = 301
            self.additive(0)
            self.state = 302
            self.match(TypstGrammarParser.DIF)
            self.state = 303
            self.symbol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(TypstGrammarParser.QUOTE)
            else:
                return self.getToken(TypstGrammarParser.QUOTE, i)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)




    def text(self):

        localctx = TypstGrammarParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(TypstGrammarParser.QUOTE)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 306
                    self.matchWildcard() 
                self.state = 311
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 312
            self.match(TypstGrammarParser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCENT_OP(self):
            return self.getToken(TypstGrammarParser.ACCENT_OP, 0)

        def L_PAREN(self):
            return self.getToken(TypstGrammarParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TypstGrammarParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(TypstGrammarParser.R_PAREN, 0)

        def getRuleIndex(self):
            return TypstGrammarParser.RULE_accent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccent" ):
                listener.enterAccent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccent" ):
                listener.exitAccent(self)




    def accent(self):

        localctx = TypstGrammarParser.AccentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_accent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(TypstGrammarParser.ACCENT_OP)
            self.state = 315
            self.match(TypstGrammarParser.L_PAREN)
            self.state = 316
            self.expr()
            self.state = 317
            self.match(TypstGrammarParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Symbol_baseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_BASE(self):
            return self.getToken(TypstGrammarParser.SYMBOL_BASE, 0)

        def text(self):
            return self.getTypedRuleContext(TypstGrammarParser.TextContext,0)


        def accent(self):
            return self.getTypedRuleContext(TypstGrammarParser.AccentContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_symbol_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol_base" ):
                listener.enterSymbol_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol_base" ):
                listener.exitSymbol_base(self)




    def symbol_base(self):

        localctx = TypstGrammarParser.Symbol_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_symbol_base)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(TypstGrammarParser.SYMBOL_BASE)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.text()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.accent()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol_base(self):
            return self.getTypedRuleContext(TypstGrammarParser.Symbol_baseContext,0)


        def subargs(self):
            return self.getTypedRuleContext(TypstGrammarParser.SubargsContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol" ):
                listener.enterSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol" ):
                listener.exitSymbol(self)




    def symbol(self):

        localctx = TypstGrammarParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.symbol_base()
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 325
                self.subargs()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(TypstGrammarParser.NUMBER, 0)

        def symbol(self):
            return self.getTypedRuleContext(TypstGrammarParser.SymbolContext,0)


        def getRuleIndex(self):
            return TypstGrammarParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = TypstGrammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_atom)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(TypstGrammarParser.NUMBER)
                pass
            elif token in [17, 28, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.symbol()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.relation_sempred
        self._predicates[3] = self.additive_sempred
        self._predicates[4] = self.mp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def relation_sempred(self, localctx:RelationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def additive_sempred(self, localctx:AdditiveContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mp_sempred(self, localctx:MpContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




