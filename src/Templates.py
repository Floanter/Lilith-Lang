class Template:

    def requiredImports(self):
        return f'#include <stdio.h>\n'
    ################################################################
    ################################################################
    #                           functio                             #
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
    def mainLilith(self, arguments, inside):
        function = f'void _MaInLiLith_({arguments})\n{{\n{inside}\n}}\n'
        return function

   
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
    def variable(self, identifier, type, value):
        return f'{type} {identifier} = {value};\n'

    def array(self, identifier, type, size, value):
        return f'{type} {identifier}{size} = {value};\n'
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
    def array_values(self, values: list):
        arrayValues = f'{{{values[1]}'

        if len(values ) > 1:
            for i in range(len(values) + 1):
                arrayValues += f'{values[i]}'
        arrayValues += '}'

        return arrayValues
    ################################################################
    ################################################################
    #                           VALUES                             #
    ################################################################
    ################################################################