from src.Parser import LilithParser

parser = LilithParser()

with open('examples/io.spell', 'r') as f:
    tokens = parser.parse(f.read())
    print(tokens.pretty())
