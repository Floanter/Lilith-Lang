from src.Parser import LilithParser
from src.CodeGen import CodeGen

parser = LilithParser()
cg = CodeGen()

with open('pruebas.spell', 'r') as f:
    tokens = parser.parse(f.read())
    cg.generate(tokens)
    #print(tokens.pretty())
