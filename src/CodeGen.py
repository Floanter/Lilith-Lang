from src.Templates import Templates
from src.Parser import LilithParser

class CodeGen():
    def __init__(self):
        self.file = ''
        self.headers = []
        self.builtins = []
        self.parser = LilithParser()
        self.templates = Templates()

    def generate(self, tokens):
        for file in tokens.children:
            if file.data == 'file':
                self.file += self._file(file)
                #print(self.file)

    ################################################################################################
    ################################################################################################
    #                                               FILE
    ################################################################################################
    ################################################################################################

    def _file(self, tokens):
        file = ''
        for block in tokens.children:
            blockType = block.data
            if blockType == 'block':
                file += self._block(block)

        return file

    ################################################################################################
    ################################################################################################
    #                                               FILE
    ################################################################################################
    ################################################################################################

    def _builtin(self, tokens):
        pass
    
    ################################################################################################
    ################################################################################################
    #                                            BLOCK
    ################################################################################################
    ################################################################################################
    def _block(self, tokens):
        block = ''
        for token in tokens.children:
            
            tokenType = token.data
            print(tokenType)
            if tokenType == 'namespace':
                block += self._namespace(token)

            if tokenType == 'template':
                block += self._template(token)

            if tokenType == 'overflow_box_access_value':
                block += self._overflow_box_access_value(token)

            if tokenType == 'namespace_access_call':
                block += self._namespace_access_call(token)

            if tokenType == 'import_lilith_builtin':
                block += self._import_lilith_builtin(token)

            #                   FUNCTIONS                       #
            if tokenType == 'main_function':
                block += self._main_function(token)
            #                   FUNCTIONS                       #

            
            #                   VARIABLES                       #
            if tokenType == 'variable_declaration':
                block += self._variable_declaration(token)

            if tokenType == 'variable_declaration_assign':
                block += self._variable_declaration_assign(token)

            if tokenType == 'const_variable_declaration_assign':
                block += self._const_variable_declaration_assign(token)

            if tokenType == 'variable_reasign':
                block += self._variable_reasign(token)

            if tokenType == 'variable_increment':
                block += self._variable_increment(token)

            if tokenType == 'variable_decrement':
                block += self._variable_decrement(token)

            if tokenType == 'array_variable_declaration_assign':
                block += self._array_variable_declaration_assign(token)

            if tokenType == 'array_variable_declaration':
                block += self._array_variable_declaration(token)

            if tokenType == 'array_variable_reasign':
                block += self._array_variable_reasign(token)
            #                   VARIABLES                       #
        
        return block

    ################################################################################################
    ################################################################################################
    #                                            BLOCK
    ################################################################################################
    ################################################################################################



    ################################################################################################
    ################################################################################################
    #                                           VARIABLES
    ################################################################################################
    ################################################################################################
    def _variable_declaration(self, tokens):
        type = ''
        identifier = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'type':
                type += self._type(token)

            if tokenType == 'identifier':
                identifier += self._type(token)

        return self.templates.variable_declaration(type, identifier)

    def _variable_declaration_assign(self, tokens):
        type = ''
        identifier = ''
        assign_operator = ''
        value = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'type':
                type += self._type(token)

            if tokenType == 'identifier':
                identifier += self._type(token)

            if tokenType == 'assign_operator':
                assign_operator += self._assign_operator(token)

            if tokenType == 'value':
                value += self._value(token)
        return self.templates.variable_declaration_assign(type, identifier, assign_operator, value)

    def _const_variable_declaration_assign(self, tokens):
        type = ''
        identifier = ''
        assign_operator = ''
        value = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'type':
                type += self._type(token)

            if tokenType == 'identifier':
                identifier += self._type(token)

            if tokenType == 'assign_operator':
                assign_operator += self._assign_operator(token)

            if tokenType == 'value':
                value += self._value(token)
        return self.templates.const_variable_declaration_assign(type, identifier, assign_operator, value)

    def _variable_reasign(self, tokens):
        identifier = ''
        assign_operator = ''
        value = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'identifier':
                identifier += self._type(token)

            if tokenType == 'assign_operator':
                assign_operator += self._assign_operator(token)

            if tokenType == 'value':
                value += self._value(token)
        return self.templates.variable_reasign(identifier, assign_operator, value)

    def _variable_increment(self, tokens):
        identifier = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'identifier':
                identifier += self._identifier(token)

        return self.templates.variable_increment(identifier)

    def _variable_decrement(self, tokens):
        identifier = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'identifier':
                identifier += self._identifier(token)

        return self.templates.variable_decrement(identifier)

    def _array_variable_declaration_assign(self, tokens):
        type = ''
        identifier = ''
        array_size = ''
        assign_operator = ''
        values = []
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'type':
                type += self._type(token)
            
            if tokenType == 'identifier':
                identifier += self._identifier(token)

            if tokenType == 'array_size':
                for number in token.children:
                    array_size += number

            if tokenType == 'assign_operator':
                assign_operator += self._assign_operator(token)

            if tokenType == 'value':
                values.append(self._value(token))

        return self.templates.array_variable_declaration_assign(type, identifier, array_size, assign_operator, values)

    def _array_variable_declaration(self, tokens):
        type = ''
        identifier = ''
        array_size = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'type':
                type += self._type(token)
            
            if tokenType == 'identifier':
                identifier += self._identifier(token)

            if tokenType == 'array_size':
                for number in token.children:
                    array_size += number

        return self.templates.array_variable_declaration(type, identifier, array_size)

    def _array_variable_reasign(self, tokens):
        identifier = ''
        array_size = ''
        assign_operator = ''
        value = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            
            if tokenType == 'identifier':
                identifier += self._identifier(token)

            if tokenType == 'array_size':
                for number in token.children:
                    array_size += number

            if tokenType == 'assign_operator':
                assign_operator += self._assign_operator(token)

            if tokenType == 'value':
                value += self._value(token)

        return self.templates.array_variable_reasign(identifier, array_size, assign_operator, value)
    ################################################################################################
    ################################################################################################
    #                                           VARIABLES
    ################################################################################################
    ################################################################################################

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

    ################################################################################################
    ################################################################################################
    #                                           VALUE
    ################################################################################################
    ################################################################################################
    def _value(self, tokens):
        value = ''
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)

            if tokenType == 'identifier':
                value += self._identifier(token)

            if tokenType == 'ellipsis_string':
                value += self._ellipsis_string(token)

            if tokenType == 'number':
                value += self._number(token)

            if tokenType == 'arithmetic':
                value += self._arithmetic(token)
            
        return value
    ################################################################################################
    ################################################################################################
    #                                           VALUE
    ################################################################################################
    ################################################################################################

    def _arithmetic(self, tokens):
        values = []
        arithmetic_signs = []
        for token in tokens.children:
            tokenType = token.data
            #print(tokenType)
            if tokenType == 'arithmetic_sign':
                arithmetic_signs.append(self._arithmetic_sign(token))

            if tokenType == 'value':
                values.append(self._value(token))
        return self.templates.arithmetic(arithmetic_signs, values)

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

    def _arithmetic_sign(self, tokens):
        arithmetic_sign = ''
        for token in tokens.children:
            arithmetic_sign += token
        return arithmetic_sign

    def _assign_operator(self, tokens):
        assign_operator = ''
        for token in tokens.children:
            assign_operator += token
        return token

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

    def _number(self, tokens):
        number = ''
        for token in tokens.children:
            number += token
        return number

    def _ellipsis_string(self, tokens):
        string = ''
        for token in tokens.children:
            string += token
        return string