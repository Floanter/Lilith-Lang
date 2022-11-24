from src.Parser import LilithParser
from src.CodeConverter import CodeConverter
import os
class Compile:
    def __init__(self) -> None:
        self.execution_path = ''
        self.main_file_path = ''

        self.build_path = ''

        self.parser = LilithParser()
        self.codeConverter = CodeConverter()


    def run(self, execution_path: str, main_file_path: str) -> None:
        self.execution_path += execution_path
        self.main_file_path += main_file_path

        self._generate_tokens()

    def _generate_tokens(self):
        path = self.execution_path + '/' + self.main_file_path
        with open(path, 'r') as f:
            tokens = self.parser.parse(f.read())
            self._convert_code(tokens)
            print(self.codeConverter.file)
            self._generate_directories()
            self._generateFile(self.codeConverter.file)
            

    def _convert_code(self, tokens):
        self.codeConverter.run(tokens)

    def _generate_directories(self):
        self.build_path += self.execution_path + '/' + '.lilbuild'
        if not os.path.exists(self.build_path):
            os.mkdir(self.build_path)

    def _generateFile(self, file):
        f = open(self.build_path + '/' + 'main.cpp', "w")
        f.write(file)
        f.close()

