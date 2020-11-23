# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from main import tokens

'''Reglas agregadas por Bryan Loor
p_codigo 
p_algoritmo
p_asignacion
p_sentenciaWhile
p_expresion
p_operadorComp
p_variables
'''
'''Reglas agregadas por Nicole Asqui
p_sentenciaFor 
p_range
p_puts
p_unless
'''

def p_codigo(p):
    '''codigo : algoritmo
                | algoritmo codigo
    '''
def p_algoritmo(p):
    ''' algoritmo : asignacion
                    | expresion
                    | comparacion
                    | sentenciaWHILE
                    | sentenciaFOR
                    | puts
                    | unless
    '''

def p_unless(p):
    ''' unless : UNLESS comparacion codigo END
    '''
def p_sentenciaFor(p):
    ''' sentenciaFOR : FOR variables IN range DO codigo END
    '''

def p_range(p):
    ''' range : ENTERO RANGO ENTERO
    '''

def p_puts(p):
    ''' puts : PUTS CADENA
    '''


def p_sentenciaWhile(p):
    '''sentenciaWHILE : WHILE  comparacion DO codigo END
    '''


def p_asignacion(p):
    '''asignacion : variables IGUAL expresion
    '''

def p_expresion(p):
    '''expresion : valor
    '''

def p_expresion_aritmetica(p):
    'expresion : valor operadorMat expresion'

def p_comparacion(p):
    'comparacion : expresion operadorComp expresion'

def p_operadorMat(p):
    '''operadorMat : MAS
                | RESTA
                | PROD
                | DIVISION
                | POTENCIA
    '''
def p_operadorComp(p):
    '''operadorComp : MAYOR
                | MENOR
                | IGUAL
                | DIFERENTE
    '''


def p_valor(p):
    '''valor : ENTERO
                | variables
                | CADENA
                | HASH

    '''

def p_variables(p):
    """ variables : VARIABLE_LOCAL
                | VARIABLE_GLOBAL
                | VARIABLE_OBJETO
                | VARIABLE_CLASE
                | CONSTANTE
    """


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

def leerAlgoritmo(file):
    s = file.read()
    print(s)
    result = parser.parse(s)
    print(result)
    file.close()

archivo1 = open("../archivos/algoritmoLoor.txt")
archivo2 = open("../archivos/algoritmoAsqui.txt")
'''
leerAlgoritmo(archivo1)
leerAlgoritmo(archivo2)
'''


