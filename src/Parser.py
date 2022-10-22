from lark import Lark
from lark.indenter import Indenter

class LilithIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

class LilithParser:
    def __init__(self):
        with open('lilith.lark', 'r') as f:
            self._lark_gramar = f.read()
            self._parser = Lark(self._lark_gramar, start='start', parser='lalr', postlex=LilithIndenter())

    def parse(self, file):
        return self._parser.parse(file)

    def parsePretty(self, file):
        return self.parse(file).pretty()