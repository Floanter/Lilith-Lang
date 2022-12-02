from src.Templates import Template
from src.Parser import LilithParser

class CodeConverter():
    def __init__(self):
        self.file = ''

        self.spellsToAdd = []

        self.mainFunctionExists = False

        self.parser = LilithParser()
        self.templates = Template()

        self.libs = {
            'io': 'libs/io.spell'
        }

        self.operators = {
            'equal':            ' = ',
            "plus":             ' + ',
            'plusplus':         '++',
            'minusminus':       '--',
            'minus':            ' - ',
            'multi':            ' * ',
            'divide':           ' / ',
            'percent':          ' % ',
            'plus_equal':       ' += ',
            'minus_equal':      ' -= ',
            'multi_equal':      ' *= ',
            'percent_equal':    ' %= ',
            'or_equal':         ' |= ',
            'power_equal':      " ^= ",
            'left_parent':      '(',
            'right_parent':     ')',
            'and':              ' && ',
            'or':               ' || ',
            'equal_to':         ' == ',
            'not_equal':        ' != ',
            'greater':          ' > ',
            'less':             ' < ',
            'greater_equal':    ' >= ',
            'less_equal':       ' <= '
        }

        self.special_word = {
            'const': 'const ',
            'static': 'static '
        }

        self.reserved_word = {
            'break': 'break;\n',
            'continue': 'continue;\n'
        }

        self._block_commands = {
            'variable': self._variable,
            'mainfn': self._mainFunction,
            'function': self._function,
            'return': self._return,
            'call': self._call,
            'if': self._if,
            'switch': self._switch,
            'while': self._while,
            'do_while': self._do_while,
            'for': self._for,
            'interface': self._interface,
            'newtype': self._newtype,
            'macro': self._macro,
            'lib_spell': self._lib_spell
        }

        self._variable_commands = {
            'identifier': self._value,
            'type': self._value,
            'value': self._value,
            'array_size': self._value,
            'array_values': self._array_values,
            'operator': self._value,
            'assignment': self._value
        }

        self._interface_commands = {
            'identifier': self._value,
            'property': self._property
        }

        self._macro_commands = {
            'identifier': self._value,
            'value': self._value,
            'macro_parameter': self._macro_parameter,
            'block': self._macro_block
        }

        self._property_commands = {
            'identifier': self._value,
            'type': self._value,
            'array_size': self._value,
            'parameters': self._parameters,
        }

        self._function_commands = {
            'type': self._value,
            'identifier': self._value,
            'parameters': self._parameters,
            'block': self._block
        }

        self._if_commands = {
            'condition': self._value,
            'block': self._block,
            'elif': self._elif,
            'else': self._else
        }

        self._elif_commands = {
            'condition': self._value,
            'block': self._block
        }

        self._switch_commands = {
            'value': self._value,
            'operator': self._value,
            'when': self._when,
            'default': self._default
        }

        self._when_commands = {
            'value': self._value,
            'operator': self._value,
            'block': self._block
        }

        self._while_commands = {
            'condition': self._value,
            'block': self._block
        }

        self._for_commands = {
            'variable': self._variable,
            'condition': self._value,
            'block': self._block
        }

        self._newtype_commands = {
            'type': self._value,
            'identifier': self._value
        }

        self._value_command = {
            'value': self._value,
            'identifier': self._value,
            'operator': self._value,
            'call': self._call,
            'key_value': self._key_value,
            'type_cast': self._type_cast
        }

    def run(self, tokens):
        self.file += self.templates.requiredImports()       
        tmpFile = self._file(tokens)
        if self.mainFunctionExists:
            tmpFile += self.templates.cMain()
        if self.spellsToAdd:
            for spell in self.spellsToAdd:
                self.file += spell
        self.file += tmpFile
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
                if blockType in self._block_commands:
                    block += self._block_commands[blockType](b)
                elif blockType in self.reserved_word:
                    block += self.reserved_word[blockType]
        return block

    ################################################################
    ################################################################
    #                           IMPORT                             #
    ################################################################
    ################################################################
    def _lib_spell(self, tokens):
        name = ''
        for t in tokens.children:
            if t.data == 'identifier':
                name += self._value(t)
        if name in self.libs:
            with open(self.libs[name], "r") as l:
                tks = self.parser.parse(l.read())
                l.close()
                f = self._file(tks)
                if f not in self.spellsToAdd:
                    self.spellsToAdd.append(f)
        return ''
    def _local_spell(self, tokens):
        name = ''
        for t in tokens.children:
            name += self._value(t)
        with open(name, "r") as l:
            tks = self.parser.parse(l.read())
            l.close()
            f = self._file(tks)
            if f not in self.spellsToAdd:
                self.spellsToAdd.append(f)
        return ''
    ################################################################
    ################################################################
    #                           IMPORT                             #
    ################################################################
    ################################################################

    ################################################################
    ################################################################
    #                        STRUCTURE                             #
    ################################################################
    ################################################################
    def _interface(self, tokens):
        i = {
            'identifier': '',
            'property': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._interface_commands:
                i[tokentype] += self._interface_commands[tokentype](token)
        return self.templates.structure(i)

    def _property(self, tokens):
        p = {
            'identifier': '',
            'type': '',
            'array_size': '',
            'parameters': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._property_commands:
                p[tokentype] += self._property_commands[tokentype](token)
        return self.templates.propertyt(p)
    ################################################################
    ################################################################
    #                        STRUCTURE                             #
    ################################################################
    ################################################################

    ################################################################
    ################################################################
    #                            MACRO                             #
    ################################################################
    ################################################################
    def _macro(self, tokens):
        macro = {
            'identifier': '',
            'value': '',
            'macro_parameter': '',
            'block': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._macro_commands:
                macro[tokentype] += self._macro_commands[tokentype](token)
        return self.templates.macro(macro)

    def _macro_block(self, tokens):
        b = self._block(tokens).replace(";", "").replace("\n", "")
        return f' \\\n{b}'

    def _macro_parameter(self, tokens):
        parameters = ''
        count = 0
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype == 'identifier':
                if count > 0:
                    parameters += ', '
                parameters += self._value(token)
                count += 1
        return parameters
    ################################################################
    ################################################################
    #                            MACRO                             #
    ################################################################
    ################################################################

    ################################################################
    ################################################################
    #                         FUNCTION                             #
    ################################################################
    ################################################################
    def _mainFunction(self, tokens):
        self.mainFunctionExists = True
        inside = ''
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype == 'block':
                inside += self._block(token)
        return self.templates.mainLilith(inside)

    def _function(self, tokens):
        function = {
            'type': '',
            'identifier': '',
            'parameters': '',
            'block': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._function_commands:
                if tokentype == 'identifier':
                    tempIdentifier = self._function_commands[tokentype](token)
                    if tempIdentifier == 'main':
                        self.mainFunctionExists = True
                        function['identifier'] += '_MAINLILITHFUNC_'
                    else:
                        function['identifier'] += tempIdentifier
                else:
                    function[tokentype] += self._function_commands[tokentype](token)
        return self.templates.function(function)

    def _call(self, tokens):
        call = {
            'identifier': '',
            'call_params': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype == 'identifier':
                call['identifier'] += self._value(token)
            elif tokentype == 'call_params':
                call['call_params'] += self._call_params(token)
        return self.templates.call(call)
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
    def _if(self, tokens):
        i = {
            'condition': '',
            'block': '',
            'elif': '',
            'else': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._if_commands:
                i[tokentype] += self._if_commands[tokentype](token)
            elif tokentype in self.operators:
                i['condition'] += self.operators[tokentype]
        #print(i)
        return self.templates.ift(i)

    def _elif(self, tokens):
        eli = {
            'condition': '',
            'block': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._elif_commands:
                eli[tokentype] += self._elif_commands[tokentype](token)
            elif tokentype in self.operators:
                eli['condition'] += self.operators[tokentype]
        return self.templates.elift(eli)

    def _else(self, tokens):
        block = ''
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype == 'block':
                block += self._block(token)
        return self.templates.elset(block)

    def _switch(self, tokens):
        switch = {
            'expression': '',
            'when': '',
            'default': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._switch_commands:
                if tokentype == 'value' or tokentype == 'operator':
                    switch['expression'] += self._switch_commands[tokentype](token)
                else:
                    switch[tokentype] += self._switch_commands[tokentype](token)
        return self.templates.switch(switch)

    def _when(self, tokens):
        when = {
            'condition': '',
            'block': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._when_commands:
                if tokentype == 'value' or tokentype == 'operator':
                    when['condition'] += self._when_commands[tokentype](token)
                elif tokentype in self.operators:
                    when['condition'] += self.operators[tokentype]
                else:
                    when[tokentype] += self._when_commands[tokentype](token)
        return self.templates.when(when)

    def _default(self, tokens):
        block = ''
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype == 'block':
                block += self._block(token)
        return self.templates.default(block)
    ################################################################
    ################################################################
    #                        CONDITIONAL                           #
    ################################################################
    ################################################################
    
    ################################################################
    ################################################################
    #                            LOOPS                             #
    ################################################################
    ################################################################
    def _while(self, tokens):
        w = {
            'condition': '',
            'block': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._while_commands:
                w[tokentype] += self._while_commands[tokentype](token)
            elif tokentype in self.operators:
                w['condition'] += self.operators[tokentype]
        return self.templates.whilet(w)

    def _do_while(self, tokens):
        w = {
            'condition': '',
            'block': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._while_commands:
                w[tokentype] += self._while_commands[tokentype](token)
            elif tokentype in self.operators:
                w['condition'] += self.operators[tokentype]
        return self.templates.doWhile(w)

    def _for(self, tokens):
        f = {
            'variable': [],
            'condition': '',
            'block': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self.operators:
                f['condition'] += self.operators[tokentype]
            elif tokentype in self._for_commands:
                if tokentype == 'variable':
                    f['variable'].append(self._for_commands[tokentype](token))
                else:
                    f[tokentype] += self._for_commands[tokentype](token)
        print(f)
        return self.templates.fort(f)
    ################################################################
    ################################################################
    #                            LOOPS                             #
    ################################################################
    ################################################################

    ################################################################
    ################################################################
    #                         VARIABLE                             #
    ################################################################
    ################################################################
    def _variable(self, tokens):
        variable = {
            'special_word': '',
            'identifier': '',
            'type': '',
            'value': '',
            'array_size': '',
            'assignment': ''
        }
        for token in tokens.children:
            tokentype = token.data
            #print(tokentype)
            if tokentype in self._variable_commands:
                if tokentype == 'array_values' or tokentype == 'operator':
                    variable['value'] += self._variable_commands[tokentype](token)
                elif tokentype == 'array_size':
                    variable['value'] += '['
                    variable['value'] += self._variable_commands[tokentype](token)
                    variable['value'] += ']'
                else:
                    variable[tokentype] += self._variable_commands[tokentype](token)
            if tokentype in self.special_word:
                variable['special_word'] += self.special_word[tokentype]
        return self.templates.variable(variable)
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
    def _newtype(self, tokens):
        nt = {
            'identifier': '',
            'type': ''
        }
        for t in tokens.children:
            tokentype = t.data
            #print(tokentype)
            if tokentype in self._newtype_commands:
                nt[tokentype] += self._newtype_commands[tokentype](t)
        return self.templates.typedef(nt)

    def _return(self, tokens):
        ret = 'return '
        options = ['value', 'operator']
        for t in tokens.children:
            tokentype = t.data
            #print(tokentype)
            if tokentype in options:
                ret += self._value(t)
        ret += ';\n'
        return ret

    def _call_params(self, tokens):
        params = []
        for t in tokens.children:
            params.append(self._value(t).replace(';', '').replace('\n', ''))
        return self.templates.parameters(params)

    def _array_values(self, tokens):
        values = []
        for t in tokens.children:
            tokentype = t.data
            #print(tokentype)
            if tokentype == 'value':
                values.append(self._value(t))
            if tokentype == 'array_values':
                values.append(self._array_values(t))

        return self.templates.array_values(values)

    def _key_value(self, tokens):
        kv = []
        for t in tokens.children:
            if t.data == 'value':
                kv.append(self._value(t))
        return f'{kv[0]} : {kv[1]}'

    def _type_cast(self, tokens):
        ty = '('
        for t in tokens.children:
            if t.data == 'type':
                ty += self._value(t)
        ty += ')'
        return ty

    def _parameters(self, tokens):
        params = []
        for t in tokens.children:
            tokentype = t.data
            if tokentype == 'parameter':
                params.append(self._parameter(t))
        return self.templates.parameters(params)

    def _parameter(self, tokens):
        identifier = ''
        type = ''
        for t in tokens.children:
            tokentype = t.data
            if tokentype == 'identifier':
                identifier += self._value(t)
            if tokentype == 'type':
                type += self._value(t)
        return f'{type} {identifier}'

    def _value(self, blocks):
        value = ''
        
        for t in blocks.children:
            if hasattr(t, 'data'):
                tokenType = t.data
                #print(tokenType)
                if tokenType in self._value_command:
                    value += self._value_command[tokenType](t)
                if tokenType == 'array_size':
                    value += '['
                    value += self._value(t)
                    value += ']'
                if tokenType in self.operators:
                    value += self.operators[tokenType]
            else:
                #print(t)
                value += t
        return value

    ################################################################
    ################################################################
    #                           VALUES                             #
    ################################################################
    ################################################################