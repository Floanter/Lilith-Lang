from ast import arguments
from src.Templates import Template
from src.Parser import LilithParser

class CodeConverter():
    def __init__(self):
        self.file = ''
        self.future_files_to_convert = []
        self.lilith_builtins = []
        self.c_builtins = []
        self.headers = []
        self.parser = LilithParser()
        self.templates = Template()

    def run(self, tokens):
        self.file += self._file(tokens)

    def _file(self, blocks):
        file = ''
        for block in blocks.children:
            file  += self._block(block)

        return file

    def _block(self, blocks):
        block = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)

                #           IMPORT         #
                if blockType == 'import':
                    block += self._import(b)

                if blockType == 'c_include':
                    block += self._c_include(b)
                
                if blockType == 'header_c':
                    block += self._header_c(b)
                #           IMPORT         #

                #          FUNCTIONS       #
                if blockType == 'main_function':
                    block += self._main_function(b)
                #          FUNCTIONS       #

        return block

    ################################################################
    ################################################################
    #                           IMPORT                             #
    ################################################################
    ################################################################
    def _import(self, blocks):
        imp = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'builtin_spell':
                    imp += self._builtin_spell(b)

                if blockType == 'custom_spell':
                    imp += self._custom_spell(b)
        return imp

    def _c_include(self, blocks):
        imp = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                print(blockType)
                
                if blockType == 'builtin_c':
                    imp += self._builtin_c(b)
        return imp

    def _builtin_spell(self, blocks):
        lib = ''
        for b in blocks.children:
            lib += b   
        if lib not in self.builtins:
            self.builtins.append(lib)
        return ''

    def _builtin_c(self, blocks):
        lib = ''
        for b in blocks.children:
            lib += b   
        if lib not in self.c_builtins:
            self.c_builtins.append(lib)
        return ''

    def _custom_spell(self, blocks):
        spell = ''
        for b in blocks.children:
            spell += b
        self.future_files_to_convert.append(spell)
        return ''

    def _header_c(self, blocks):
        header = ''
        for b in blocks.children:
            header += b
        if header not in self.headers:
            self.headers.append(header)
        return ''
    ################################################################
    ################################################################
    #                           IMPORT                             #
    ################################################################
    ################################################################



    ################################################################
    ################################################################
    #                         FUNCTION                             #
    ################################################################
    ################################################################
    def _main_function(self, blocks):
        arguments = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'arguments':
                    arguments += self._arguments(b)
        return ''

    def _arguments(self, blocks):
        arguments = []
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'argument':
                    arguments.append(self._argument(b))
                
        return ''

    def _argument(self, blocks):
        identifier = ''
        type = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'identifier':
                    identifier += self._identifier(b)
                
                if blockType == 'type':
                    type += self._type(b)

                if blockType == 'embed_type':
                    type += self._embed_type(b)
                
        return ''
    ################################################################
    ################################################################
    #                         FUNCTION                             #
    ################################################################
    ################################################################



    ################################################################
    ################################################################
    #                       IDENTIFIER                             #
    ################################################################
    ################################################################
    def _identifier(self, blocks):
        identifier = ''
        for i in blocks.children:
            identifier += i
        return identifier

    def _type(self, blocks):
        type = ''
        for t in blocks.children:
            type += t
        return type

    def _embed_type(self, blocks):
        type = ''
        embed_type = ''
        for t in blocks.children:
            if hasattr(t, 'children'):
                for et in t.children:
                    embed_type += et
            else:
                type += t
        return f'{type}"<{embed_type}>'
    ################################################################
    ################################################################
    #                       IDENTIFIER                             #
    ################################################################
    ################################################################