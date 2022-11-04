from ast import arguments


class Templates:
    def __init__(self):
        pass
class Template:
    ################################################################
    ################################################################
    #                           functio                             #
    ################################################################
    ################################################################
    def builtin_c(self, name):
        return f'#include <{name}>\n'
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
    def mainLilith(self, arguments, inside):
        function = f'void _MaInLiLith_({arguments})\n{{\n{inside}\n}}\n'
        return function

    def function(self, type, identifier, arguments, inside):
        return f'{type} {identifier}({arguments})\n{{\n{inside}\n}}\n'

    def declare(self, type, identifier, arguments):
        return f'{type} {identifier}({arguments});\n'

    def call(self, identifier, semicolon = True):
        if semicolon:
            return f'{identifier}();\n'
        return f'{identifier}()'

    def callWithParams(self, identifier, parameters, semicolon=True):
        if semicolon:
            return f'{identifier}({parameters});\n'
        return f'{identifier}({parameters})'

    def argument(self, type, identifier):
        return f'{type} {identifier}'

    def arguments(self, arguments):
        a = f'{arguments[0]}'
        if len(arguments) > 1:
            for i in range(1, len(arguments)):
                a += f', {arguments[i]}'
        return a

    def parameters(self, parameters):
        p = f'{parameters[0]}'
        if len(parameters) > 1:
            for i in range(1, len(parameters)):
                p += f', {parameters[i]}'
        return p
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
    def if_condition(self, condition, inside):
        return f'if({condition})\n{{\n{inside}\n}}\n'

    def condition(self, values, condition):
        if len(values) > 1:
            return f'{values[0]} {condition} {values[1]}'
        return f'{values[0]}'
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
    def var_declaration_assign(self, var, value):
        return f'{var} = {value};\n'

    def var_declaration(self, var):
        return f'{var};\n'

    def var_reassign_value(self, identifier, reassign_operator, value):
        return f'{identifier} {reassign_operator} {value};\n'

    def var_reassign(self, identifier, reassign_operator):
        return f'{identifier}{reassign_operator};\n'
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

    ################################################################
    ################################################################
    #                           VALUES                             #
    ################################################################
    ################################################################