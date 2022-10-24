from src.Parser import LilithParser

parser = LilithParser()

with open('examples/templates.spell', 'r') as f:
    tokens = parser.parse(f.read())
    print(tokens.pretty())
