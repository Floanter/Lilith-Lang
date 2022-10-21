from turtle import width
from src.Parser import LilithParser

parser = LilithParser()

with open('examples/imports.spell', 'r') as f:
    print(parser.parsePretty(f.read()))