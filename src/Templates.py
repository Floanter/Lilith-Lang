class Templates:
    def __init__(self):
        pass

    def default_includes(self):
        return f'#include <iostream>\n'

    def function(self, type, identifier, parameters, insideCode):
        return f'{type} {identifier}({parameters})\n{{\n    {insideCode}\n}}\n'

    def mainFunction(self, insideCode, arguments=None):
        if arguments:
            return f'void _mainLilith_({arguments})\n{{\n{insideCode}\n}}\n\nint main()\n{{\n_mainLilith_();\nreturn 0;\n}}\n'
        return f'void _mainLilith_()\n{{\n{insideCode}\n}}\n\nint main()\n{{\n_mainLilith_();\nreturn 0;\n}}\n'

    def namespace(self, name, code):
        return f'namespace {name}\n{{\n {code}\n}}\n'

    def namespace_access_call(self, identifier, call):
        return f'{identifier}::{call}'

    def namespace_access_identifier(self, identifiers):
        namespace_access_identifier = f'{identifiers[0]}'

    
        for i in range(1, len(identifiers)):
            namespace_access_identifier += f'::{identifiers[i]}'

        return namespace_access_identifier

    def overflow(self, namespace_identifier, operator, value):
        overflow = f'{namespace_identifier[0]}'

        if len(operator) > 1 :
            for i in range(0, len(operator)):
                overflow += f' {operator[i]} {value[i]}'
        else:
            overflow += f' {operator[0]} {value[0]}'
        overflow += ';\n'

        return overflow

    def arguments(self, types, identifiers):
        arguments = f'{types[0]} {identifiers[0]}'

        for i in range(1, len(types)):
            arguments += f', {types[i]} {identifiers[i]}'
        return arguments

    def template(self, type, function):
        return f'template< class {type} > {function}'

    def call(self, identifier, parameters):
        return f'{identifier}({parameters});\n'

    def parameters(self, values):
        parameters = f'{values[0]}'

        if len(values) > 1:
            for i in range(1, len(values)):
                parameters += f', {values[i]}'

        return parameters

    def call_with_params(self, identifier, parameters):
        return f'{identifier}({parameters});\n'

    def import_lilith_builtin(self, identifier):
        return f'#include"builtins/{identifier}.h"'
