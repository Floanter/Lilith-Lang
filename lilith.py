from turtle import width
from src.Parser import LilithParser

parser = LilithParser()

with open('examples/conditions.li', 'r') as f:
    print(parser.parsePretty(f.read()))