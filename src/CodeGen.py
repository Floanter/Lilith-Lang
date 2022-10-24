from src.Templates import Templates

class CodeGen():
    def __init__(self):
        self.files = []
        self.templates = Templates()

    def generate(self, tokens):
        for file in tokens.children:
            if file.data == 'file':
                self.files.append(self._file(file))

    def _file(self, tokens):
        file = ''
        for block in tokens.children:
            blockType = block.data
            if blockType == 'block':
                file += self._block(block)

        return file

    def _block(self, tokens):
        block = ''
        for token in tokens.children:
            tokenType = token.data
            print(tokenType)
            if tokenType == 'namespace':
                block += self._namespace(token)

            if tokenType == 'template':
                block += self._template(token)

            if tokenType == 'overflow':
                block += self._overflow(token)
        
        return block

    def _namespace(self, tokens):
        identifier = ''
        blocks = ''
        for token in tokens.children:
            tokenType = token.data

            if tokenType == 'block':
                blocks += self._block(token)

            if tokenType == 'identifier':
                identifier += self._identifier(token)

        return self.templates.namespace(identifier, blocks)

    def _template(self, tokens):
        type = ''
        function = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'type':
                type += self._type(token)

            if tokenType == 'function':
                function += self._function(token)

        return self.templates.template(type, function)

    def _function(self, tokens):
        identifier = ''
        type = ''
        insideCode = ''
        arguments = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'identifier':
                identifier += self._identifier(token)

            if tokenType == 'type':
                type += self._type(token)

            if tokenType == 'block':
                insideCode += self._block(token)

            if tokenType == 'arguments':
                arguments += self._arguments(token)

        return self.templates.function(type, identifier, arguments, insideCode)

    def _overflow(self, tokens):
        namespace_identifier = ''
        overflow_operator = ''
        value = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'namespace_access_identifier':
                namespace_identifier += self._namespace_access_identifier(token)

            if tokenType == 'overflow_operator':
                overflow_operator += self._overflow_operator(token)

            if tokenType == 'value':
                value += self._value(token)

        return self.templates.overflow(namespace_identifier, overflow_operator, value)

    def _namespace_access_identifier(self, tokens):
        identifiers = []

        for token in tokens.children:
            identifiers.append(self._identifier(token))

        return self.templates.namespace_access_identifier(identifiers)

    def _overflow_operator(self, tokens):
        operator = ''
        for token in tokens.children:
            operator += token
        return operator

    def _value(self, tokens):
        value = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)

            if tokenType == 'identifier':
                value += self._identifier(token)
            
        return value

    def _arguments(self, tokens):
        types = []
        identifiers = []
        for arguments in tokens.children:
            for token in arguments.children:
                tokenType = token.data
                #print(tokenType)
                if tokenType == 'identifier':
                    identifiers.append(self._identifier(token))

                if tokenType == 'type':
                    types.append(self._type(token))
            
        return self.templates.arguments(types, identifiers)

    def _identifier(self, tokens):
        identifier = ''
        for token in tokens.children:
            identifier += token
        return identifier

    def _type(self, tokens):
        type = ''
        for token in tokens.children:
            type += token
        return type