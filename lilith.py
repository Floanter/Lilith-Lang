from src.Parser import LilithParser

parser = LilithParser()

with open('examples/class.spell', 'r') as f:
    tokens = parser.parse(f.read())
    print(tokens.pretty())
