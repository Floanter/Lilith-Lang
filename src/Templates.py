class Templates:
    def __init__(self):
        pass

    def function(self, type, identifier, parameters, insideCode):
        return f'{type} {identifier}({parameters})\n{{\n    {insideCode}\n}}\n'

    def mainFunction(self, insideCode, parameters=None):
        if parameters:
            return f'void _mainLilith_({parameters})\n{{\n    {insideCode}}}\n\nint main()\n{{\n_mainLilith_();\nreturn 0;\n}}\n'
        return f'void _mainLilith_()\n{{\n    {insideCode}}}\n\nint main()\n{{\n_mainLilith_();\nreturn 0;\n}}\n'

    def namespace(self, name, code):
        return f'namespace {name}\n{{\n {code}\n}}\n'

    def namespace_access_identifier(self, identifiers):
        namespace_access_identifier = f'{identifiers[0]}'

    
        for i in range(1, len(identifiers)):
            namespace_access_identifier += f'::{identifiers[i]}'

        return namespace_access_identifier

    def overflow(self, namespace_identifier, operator, value):
        return f'{namespace_identifier} {operator} {value};\n'

    def arguments(self, types, identifiers):
        arguments = f'{types[0]} {identifiers[0]}'

        for i in range(1, len(types)):
            arguments += f', {types[i]} {identifiers[i]}'
        return arguments

    def template(self, type, function):
        return f'template< class {type} > {function}'