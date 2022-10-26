from src.Templates import Templates

class CodeGen():
    def __init__(self):
        self.file = ''
        self.headers = []
        self.builtins = []
        self.templates = Templates()

    def generate(self, tokens):
        for file in tokens.children:
            if file.data == 'file':
                self.file += self._file(file)
                #print(self.file)

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
            #print(tokenType)
            if tokenType == 'namespace':
                block += self._namespace(token)

            if tokenType == 'template':
                block += self._template(token)

            if tokenType == 'overflow_box_access_value':
                block += self._overflow_box_access_value(token)

            if tokenType == 'main_function':
                block += self._main_function(token)

            if tokenType == 'namespace_access_call':
                block += self._namespace_access_call(token)

            if tokenType == 'import_lilith_builtin':
                block += self._import_lilith_builtin(token)
        
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

    def _namespace_access_call(self, tokens):
        identifier = ''
        call = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'identifier':
                identifier += self._identifier(token)
            
            if tokenType == 'call_with_params':
                call += self._call_with_params(token)
        return self.templates.namespace_access_call(identifier, call)

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

    def _main_function(self, tokens):
        insideCode = ''
        arguments = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'arguments':
                arguments += self._arguments(token)

            if tokenType == 'block':
                insideCode += self._block(token)

            if tokenType == 'no_arguments':
                arguments += 'void'
                
        if arguments == 'void':
            return self.templates.mainFunction(insideCode, None)
        return self.templates.mainFunction(insideCode, arguments)

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

    def _overflow_box_access_value(self, tokens):
        namespace_identifier = []
        overflow_operator = []
        value = []

        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'namespace_access_identifier':
                namespace_identifier.append(self._namespace_access_identifier(token))

            if tokenType == 'overflow_operator':
                overflow_operator.append(self._overflow_operator(token))

            if tokenType == 'value':
                value.append(self._value(token))
        #print(self.templates.overflow(namespace_identifier, overflow_operator, value))
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

    def _call_with_params(self, tokens):
        identifier = ''
        parameters = ''

        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'identifier':
                identifier += self._identifier(token)

            if tokenType == 'parameters':
                parameters += self._parameters(token)
        return self.templates.call_with_params(identifier, parameters)

    def _import_lilith_builtin(self, tokens):
        identifier = ''
        for token in tokens.children:
            tokenType = token.data
            if tokenType == 'identifier':
                identifier += self._identifier(token)
        return self.templates.import_lilith_builtin(identifier)

    def _parameters(self, tokens):
        values = []
        for token in tokens.children:
            tokenType = token.data
            if tokenType == 'value':
                values.append(self._value(token))
        return self.templates.parameters(values)

    def _value(self, tokens):
        value = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)

            if tokenType == 'identifier':
                value += self._identifier(token)

            if tokenType == 'ellipsis_string':
                value += self._ellipsis_string(token)
            
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

    def _ellipsis_string(self, tokens):
        string = ''
        for token in tokens.children:
            string += token
        return string
