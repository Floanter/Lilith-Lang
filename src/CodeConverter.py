from src.Templates import Template
from src.Parser import LilithParser

class CodeConverter():
    def __init__(self):
        self.file = ''

        self.mainFunctionExists = False

        self.parser = LilithParser()
        self.templates = Template()

    def run(self, tokens):
        self.file += self._file(tokens)
        if self.mainFunctionExists:
            pass
        #print(self.file)

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

                #          VARIABLES       #
                if blockType == 'variable':
                    block += self._variable(b)
                #          VARIABLES       #

        return block

    ################################################################
    ################################################################
    #                           IMPORT                             #
    ################################################################
    ################################################################
    
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
    
    ################################################################
    ################################################################
    #                         FUNCTION                             #
    ################################################################
    ################################################################


    ################################################################
    ################################################################
    #                        CONDITIONAL                           #
    ################################################################
    ################################################################
    
    ################################################################
    ################################################################
    #                        CONDITIONAL                           #
    ################################################################
    ################################################################


    ################################################################
    ################################################################
    #                         VARIABLE                             #
    ################################################################
    ################################################################
    


    ################################################################
    ################################################################
    #                         VARIABLE                             #
    ################################################################
    ################################################################

    def _variable(self, tokens):
        identifier = ''
        type = ''
        value = ''

        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)

            if tokentype == 'identifier':
                identifier += self._identifier(token)
            if tokentype == 'type':
                type += self._type(token)
            if tokentype == 'value':
                value += self._value(token)
        
        return self.templates.variable(identifier, type, value)

    ################################################################
    ################################################################
    #                           VALUES                             #
    ################################################################
    ################################################################
    def _identifier(self, blocks):
        identifier = ''
        for i in blocks.children:
            identifier += i
        return identifier

    def _value(self, blocks):
        value = ''
        for t in blocks.children:
            if hasattr(t, 'data'):
                tokenType = t.data
                #print(tokenType)
                if tokenType == 'identifier':
                    value += self._identifier(t)

                if tokenType == 'call':
                    value += self._call(t, False)

                if tokenType == 'call_params':
                    value += self._call_params(t, False)
            else:
                #print(t)
                value += t
        return value

    def _arithmetic(self, blocks):
        first_value = ''
        arith_value = ''
        for t in blocks.children:
            if hasattr(t, 'data'):
                tokenType = t.data
                #print(tokenType)
                if tokenType == 'first_value':
                    first_value += self._value(t)

                if tokenType == 'arith_value':
                    arith_value += self._arith_value(t)

        return first_value + arith_value

    def _arith_value(self, blocks):
        v = ''
        for t in blocks.children:
            if hasattr(t, 'data'):
                tokenType = t.data
                print(tokenType)
                if tokenType == 'sign':
                    v += self._sign(t)

                if tokenType == 'call':
                    v += self._call(t, False)
            else:
                v += t
        return v

    def _sign(self, blocks):
        s = ''
        for t in blocks.children:
            s += t
        return s

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
        return f'{type}<{embed_type}>'

    def _reassign_operator(self, blocks):
        o = ''
        for t in blocks.children:
            o += t
        return o
    ################################################################
    ################################################################
    #                           VALUES                             #
    ################################################################
    ################################################################