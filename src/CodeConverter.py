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

                if blockType == 'function_definition':
                    block += self._function_definition(b)

                if blockType == 'function_declaration':
                    block += self._function_declaration(b)

                if blockType == 'call':
                    block += self._call(b)

                if blockType == 'call_params':
                    block += self._call_params(b)
                #          FUNCTIONS       #

                #          VARIABLES       #
                if blockType == 'var_declaration_assign':
                    block += self._var_declaration_assign(b)

                if blockType == 'var_declaration':
                    block += self._var_declaration(b)

                if blockType == 'var_reassign':
                    block += self._var_reassign(b)

                if blockType == 'var_reassign_value':
                    block += self._var_reassign_value(b)
                #          VARIABLES       #

                #        CONDITIONALS      #
                if blockType == 'if_condition':
                    block += self._if_condition(b)
                #        CONDITIONALS      #

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
        inside = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'arguments':
                    arguments += self._arguments(b)

                if blockType == 'block':
                    inside += self._block(b)
        return self.templates.mainLilith(arguments, inside)

    def _function_definition(self, blocks):
        type = ''
        identifier = ''
        arguments = ''
        inside = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'type':
                    type += self._type(b)
        
                if blockType == 'identifier':
                    identifier += self._identifier(b)
                
                if blockType == 'arguments':
                    arguments += self._arguments(b)

                if blockType == 'block':
                    inside += self._block(b)

        return self.templates.function(type, identifier, arguments, inside)

    def _function_declaration(self, blocks):
        type = ''
        identifier = ''
        arguments = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'type':
                    type += self._type(b)
        
                if blockType == 'identifier':
                    identifier += self._identifier(b)
                
                if blockType == 'arguments':
                    arguments += self._arguments(b)

        return self.templates.declare(type, identifier, arguments)

    def _call(self, blocks, semicolon= True):
        identifier = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'identifier':
                    identifier += self._identifier(b)
        return self.templates.call(identifier, semicolon)

    def _call_params(self, blocks, semicolon=True):
        identifier = ''
        parameters = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'identifier':
                    identifier += self._identifier(b)

                if blockType == 'parameters':
                    parameters += self._parameters(b)
        return self.templates.callWithParams(identifier, parameters, semicolon)

    def _arguments(self, blocks):
        arguments = []
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'argument':
                    arguments.append(self._argument(b))
        if len(arguments) < 1:
            return ''
        return self.templates.arguments(arguments)

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
       
        return self.templates.argument(type, identifier)

    def _parameters(self, blocks):
        parameters = []
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'value':
                    parameters.append(self._value(b))

                if blockType == 'arithmetic':
                    parameters.append(self._arithmetic(b))
        return self.templates.parameters(parameters)
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
    def _if_condition(self, blocks):
        conditions = []
        inside = ''
        logicals = []
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                print(blockType)
                if blockType == 'condition':
                    condition += self._condition(b)

                if blockType == 'block':
                    inside += self._block(b)

                if blockType == 'or_logical':
                    logicals.append('||')

        return self.templates.if_condition(condition, inside)

    def _condition(self, blocks):
        values = []
        condition = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'value':
                    values.append(self._value(b))
                
                if blockType == 'greater_comparison':
                    condition += '>'

                if blockType == 'less_comparison':
                    condition += '<'
        return self.templates.condition(values, condition)
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
    def _var_declaration_assign(self, blocks):
        var = ''
        value = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'normal_var_type':
                    var += self._normal_var_type(b)

                if blockType == 'const_var_type':
                    var += self._const_var_type(b)

                if blockType == 'static_var_type':
                    var += self._static_var_type(b)
                
                if blockType == 'value':
                    value += self._value(b)

        return self.templates.var_declaration_assign(var, value)

    def _var_declaration(self, blocks):
        var = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'normal_var_type':
                    var += self._normal_var_type(b)

                if blockType == 'const_var_type':
                    var += self._const_var_type(b)

                if blockType == 'static_var_type':
                    var += self._static_var_type(b)

        return self.templates.var_declaration(var)

    def _var_reassign(self, blocks):
        identifier = ''
        reassign_operator = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
            if blockType == 'identifier':
                identifier += self._identifier(b)

            if blockType == 'reassign_operator':
                reassign_operator += self._reassign_operator(b)

        return self.templates.var_reassign(identifier, reassign_operator)

    def _var_reassign_value(self, blocks):
        identifier = ''
        reassign_operator = ''
        value = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
            if blockType == 'identifier':
                identifier += self._identifier(b)

            if blockType == 'reassign_operator':
                reassign_operator += self._reassign_operator(b)

            if blockType == 'value':
                value += self._value(b)

            if blockType == 'arithmetic':
                value += self._arithmetic(b)
                
        return self.templates.var_reassign_value(identifier, reassign_operator, value)

    def _normal_var_type(self, blocks):
        type = ''
        identifier = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'identifier':
                    identifier += self._identifier(b)
                
                if blockType == 'type':
                    type += self._type(b)
                
        return f'{type} {identifier}'

    def _const_var_type(self, blocks):
        type = ''
        identifier = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'identifier':
                    identifier += self._identifier(b)
                
                if blockType == 'type':
                    type += self._type(b)
                
        return f'const {type} {identifier}'

    def _static_var_type(self, blocks):
        type = ''
        identifier = ''
        for b in blocks.children:
            if hasattr(b, 'data'):
                blockType = b.data
                #print(blockType)
                if blockType == 'identifier':
                    identifier += self._identifier(b)
                
                if blockType == 'type':
                    type += self._type(b)
                
        return f'static {type} {identifier}'

    ################################################################
    ################################################################
    #                         VARIABLE                             #
    ################################################################
    ################################################################


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