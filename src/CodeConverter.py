from src.Templates import Templates
from src.Parser import LilithParser

class CodeConverter():
    def __init__(self):
        self.file = ''
        self.headers = []
        self.builtins = []
        self.parser = LilithParser()
        self.templates = Templates()

    def run(self, tokens):
        pass