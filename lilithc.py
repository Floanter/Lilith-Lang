from src.Compile import Compile
import sys
import os

compiler = Compile()

compiler.run(os.getcwd(), sys.argv[1])