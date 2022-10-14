from lark import Lark

class LilithParser:
    def __init__(self):
        with open('lilith.lark', 'r') as f:
            self._lark_gramar = f.read()
            self._parser = Lark(self._lark_gramar, start='start')

    def parse(self, file):
        return self._parser.parse(file)

    def parsePretty(self, file):
        return self.parse(file).pretty()